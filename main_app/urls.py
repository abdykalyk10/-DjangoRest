from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/reviews/', views.movies_reviews_view),  
    path('api/v1/movies/', views.movies_api_view),
    path('api/v1/movies/<int:id>/', views.movie_detail),

    path('api/v1/directors/', views.directors_api_view), 
    path('api/v1/directors/<int:id>/', views.directors_detail),

    path('api/v1/reviews/', views.reviews_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail),
]
