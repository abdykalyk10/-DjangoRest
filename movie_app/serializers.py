from rest_framework import serializers
from .models import Movie, Review, Director

class ReviewSerializer(serializers.ModelSerializer):
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Значение stars должно быть от 1 до 5.")
        return value

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    rating = serializers.FloatField() 
    director = DirectorSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'