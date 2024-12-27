# voting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),
    path('create/', views.create_candidate, name='create_candidate'),
    path('vote/<int:candidate_id>/', views.vote_candidate, name='vote_candidate'),
    path('blockchain/', views.blockchain_view, name='blockchain_view'),
]
