
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from .serialalizers import MovieSerializer, DirectorSerializer, ReviewSerializer

#Movie
@api_view(http_method_names=['GET'])
def movies_api_view(request):
    movies = Movie.objects.filter()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data)

@api_view(http_method_names=['GET'])
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)  
    serializer = MovieSerializer(movie)  
    return Response(serializer.data)


#Director
@api_view(http_method_names=['GET'])
def directors_api_view(request):
    directors = Director.objects.filter()
    serializer = DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data)

@api_view(http_method_names=['GET'])
def directors_detail(request, id):
    movie = Director.objects.get(id=id)  
    serializer = DirectorSerializer(movie)  
    return Response(serializer.data)


#Review
@api_view(http_method_names=['GET'])
def reviews_api_view(request):
    reviews = Review.objects.filter()
    serializer = ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data)

@api_view(http_method_names=['GET'])
def reviews_detail(request, id):
    movie = Review.objects.get(id=id)  
    serializer = ReviewSerializer(movie)  
    return Response(serializer.data)

