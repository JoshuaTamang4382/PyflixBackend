from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,  # Include role
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,  # Include role
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Watchlist
from .serializers import WatchlistSerializer
from movies.models import Movie

class WatchlistAddView(generics.CreateAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associate the logged-in user with the watchlist entry
        serializer.save(user=self.request.user)

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create a watchlist entry for the movie
        return self.create(request)

class WatchlistRemoveView(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        movie_id = self.kwargs['movie_id']
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            raise Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return Watchlist.objects.get(user=user, movie=movie)

class WatchlistDetailView(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
