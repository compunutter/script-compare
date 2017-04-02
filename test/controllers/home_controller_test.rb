require 'test_helper'

class HomeControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get home_index_url
    assert_response :success
  end

  test "should get new" do
    get home_new_url
    assert_response :success
  end

  test "should get results" do
    get home_results_url
    assert_response :success
  end

end
