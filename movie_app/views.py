from django.db.models import Count, Avg
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET'])
def movies_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.prefetch_related('reviews').all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

#Director
@api_view(http_method_names=['GET'])
def directors_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def directors_detail(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)

#Review
@api_view(http_method_names=['GET'])
def reviews_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data)

@api_view(http_method_names=['GET'])
def reviews_detail(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)