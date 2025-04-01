from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrStaff  # Import the custom permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class MovieListCreateView(APIView):
    permission_classes = [IsAuthenticated,IsAdminOrStaff]  # Apply the custom permission class

    def get(self, request):
        """
        Retrieve a list of movies (allowed for all users).
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new movie (allowed only for admin or staff users).
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailView(APIView):
    permission_classes = [IsAuthenticated,IsAdminOrStaff]  # Apply the custom permission class

    def get(self, request, movie_id):
        """
        Retrieve details of a specific movie (allowed for all users).
        """
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, movie_id):
        """
        Update an existing movie (allowed only for admin or staff users).
        """
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, movie_id):
        """
        Delete an existing movie (allowed only for admin or staff users).
        """
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieListGetPublic(APIView):
    permission_classes = [AllowAny]  # Apply the custom permission class

    def get(self, request):
        """
        Retrieve a list of movies (allowed for all users).
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailPublicView(APIView):
    permission_classes = [AllowAny]  # Apply the custom permission class

    def get(self, request, movie_id):
        """
        Retrieve details of a specific movie (allowed for all users).
        """
        try:
            movie = Movie.objects.get(movie_id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    

