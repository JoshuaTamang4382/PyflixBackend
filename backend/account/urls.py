from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movie/watchlist/', WatchlistDetailView.as_view(), name='watchlist_detail'),  # GET user's watchlist
    path('movie/watchlist/add/<str:movie_id>/', WatchlistAddView.as_view(), name='watchlist_add'),  # Add movie to watchlist
    path('movie/watchlist/remove/<str:movie_id>/', WatchlistRemoveView.as_view(), name='watchlist_remove'),  # Remove movie from watchlist
]
