
from django.urls import path
from movie_app import views
from django.urls import path
from .views import DirectorsAPIView, DirectorDetailAPIView, MoviesAPIView, MovieDetailAPIView, ReviewsAPIView, ReviewDetailAPIView, MoviesReviewsAPIView

urlpatterns = [
    # Directors
    path('api/v1/directors/', DirectorsAPIView.as_view()),
    path('api/v1/directors/<int:id>/', DirectorDetailAPIView.as_view()),

    # Movies
    path('api/v1/movies/', MoviesAPIView.as_view()),
    path('api/v1/movies/<int:id>/', MovieDetailAPIView.as_view()),

    # Reviews
    path('api/v1/reviews/', ReviewsAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewDetailAPIView.as_view()),

    # Movies with reviews
    path('api/v1/movies-reviews/', MoviesReviewsAPIView.as_view()),
]
