from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

class BaseAPIView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, model, id):
        return get_object_or_404(model, id=id)

class DirectorsAPIView(BaseAPIView):
    def get(self, request):
        directors = Director.objects.all()
        return Response(DirectorSerializer(directors, many=True).data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorDetailAPIView(BaseAPIView):
    def get(self, request, id):
        director = self.get_object(Director, id)
        return Response(DirectorSerializer(director).data)

    def put(self, request, id):
        director = self.get_object(Director, id)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        director = self.get_object(Director, id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoviesAPIView(BaseAPIView):
    def get(self, request):
        movies = Movie.objects.prefetch_related('reviews').only('id', 'title', 'description', 'release_date', 'director')
        return Response(MovieSerializer(movies, many=True).data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(BaseAPIView):
    def get(self, request, id):
        movie = self.get_object(Movie, id)
        return Response(MovieSerializer(movie).data)

    def put(self, request, id):
        movie = self.get_object(Movie, id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = self.get_object(Movie, id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewsAPIView(BaseAPIView):
    def get(self, request):
        reviews = Review.objects.all()
        return Response(ReviewSerializer(reviews, many=True).data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailAPIView(BaseAPIView):
    def get(self, request, id):
        review = self.get_object(Review, id)
        return Response(ReviewSerializer(review).data)

    def put(self, request, id):
        review = self.get_object(Review, id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        review = self.get_object(Review, id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoviesReviewsAPIView(BaseAPIView):
    def get(self, request):
        movies = Movie.objects.prefetch_related('reviews').only('id', 'title', 'description', 'release_date', 'director')
        return Response(MovieSerializer(movies, many=True).data)
