class ResultsController < ApplicationController
  def index
    @sessions = Dir.entries(Rails.root.join('public', 'usercontent'))
      .select {|f| f.include?('-')}
  end

  def showsessiondetails
    session_id = params[:id]
    file_name = Rails.root.join('public', 'usercontent', session_id, 'results.txt')
    if File.exist?(file_name)
      file = File.open(file_name)
      @results = file.read
    else
      @results = "No results yet"
    end
  end

  def runsessionwithid
    session_id = params[:id]
  end
end
