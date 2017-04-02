class RunSessionScriptsJob < ApplicationJob
  queue_as :default

  def perform(session_id)
    # Our results file path including name
    results_file = Rails.root.join('public', 'usercontent', session_id, 'results.txt')
    # Delete the file if it already exists
    File.delete(results_file) if File.exist?(results_file)
    # Get all the files currently in the directory
    files = Dir.entries(Rails.root.join('public', 'usercontent', session_id))
               .select {|f| f.include?('.py')}
    # todo: select only .py files
    # Proceed if we've got more than one file
    if files.count > 0
      files.each do |f|
        times = Array.new
        file_name = Rails.root.join('public', 'usercontent', session_id, f)
        output = ''
        # Exec the file 3 times to get an avg run time
        3.times do
          start_time = Time.new
          output = `python3 #{file_name}`
          times.push(Time.new.to_ms - start_time.to_ms)
        end
        # Append the results to our results file
        size = File.size(file_name)
        # todo: file size units to output vv
        file_text = "File name: #{f}, File size: #{size} bytes, Average run time: #{times.sum/3}ms, Output:\n#{output}\n"
        File.open(results_file, 'a') { |f| f.write(file_text) }
      end
    end
  end
end
