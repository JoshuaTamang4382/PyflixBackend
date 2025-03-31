from django.urls import path
from .views import *

urlpatterns = [
    path('list/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('create/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('<str:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie-list/', MovieListGetView.as_view(), name='movie-list'),
]

