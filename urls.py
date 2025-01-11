from django.urls import path
from . import views

app_name = 'voting'  # Namespace for the voting app

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_candidate, name='create_candidate'),
    path('vote/<int:candidate_id>/', views.vote_candidate, name='vote_candidate'),
    path('blockchain/', views.blockchain_view, name='blockchain_view'),
    path('list/', views.candidate_list, name='candidate_list'),
]
