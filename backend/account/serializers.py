from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = validated_data.pop("role", "user")  # Default to 'user' if not provided
        user = User.objects.create_user(**validated_data)
        user.role = role  # Assign role separately
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


# serializers.py
from rest_framework import serializers
from .models import Watchlist
from movies.models import Movie

class WatchlistSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    
    class Meta:
        model = Watchlist
        fields = ['id', 'user', 'movie', 'added_at']
        read_only_fields = ['user', 'added_at']  # 'user' should not be set via the API directly
