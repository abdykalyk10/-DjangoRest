from rest_framework import serializers
from movie_app.models import Movie, Review, Director

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movies.count()

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    director = DirectorSerializer(read_only=True)

    def get_reviews_count(self, obj):
        return obj.reviews.count()
    
    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return 0
        total_stars = sum(review.stars for review in reviews)
        return round(total_stars / len(reviews), 1)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'director', 'reviews', 'reviews_count', 'rating']