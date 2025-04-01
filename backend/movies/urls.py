from django.urls import path
from .views import *

urlpatterns = [
    path('list/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('create/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('<str:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('public/<str:movie_id>/', MovieDetailPublicView.as_view(), name='movie-detail-public'),
    path('list/public/', MovieListGetPublic.as_view(), name='movie-list-public'),
]

