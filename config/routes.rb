Rails.application.routes.draw do

  get 'results', to: 'results#index'
  get 'results/session/:id', to: 'results#showsessiondetails'
  root to: 'home#index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
