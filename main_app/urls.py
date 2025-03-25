from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie_app/', include('movie_app.urls')),
    path('users/', include('users.urls')),
]