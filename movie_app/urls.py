from django.urls import path
from movie_app.views import movies_with_reviews, directors_list

urlpatterns = [
    path('api/v1/movies/reviews/', movies_with_reviews),
    path('api/v1/directors/', directors_list),
]
