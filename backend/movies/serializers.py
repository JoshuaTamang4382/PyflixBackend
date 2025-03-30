from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # Categories field can be read and written to
    categories = serializers.CharField()  # No write_only=True, allows for reading and writing

    class Meta:
        model = Movie
        fields = '__all__'  # Include all fields from the Movie model

    def create(self, validated_data):
        # Extract categories and split into a list
        categories_str = validated_data.pop('categories', "")
        
        # Create the movie instance
        movie = Movie.objects.create(**validated_data)
        
        # Set the categories
        movie.set_categories(categories_str.split(","))
        movie.save()
        
        return movie

    def update(self, instance, validated_data):
        # Extract categories and split into a list
        categories_str = validated_data.pop('categories', "")
        
        # Update the movie instance
        instance = super().update(instance, validated_data)
        
        # Set the categories
        instance.set_categories(categories_str.split(","))
        instance.save()
        
        return instance
