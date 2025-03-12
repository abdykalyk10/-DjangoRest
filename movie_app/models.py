from django.db import models
from django.db.models import Avg

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.count()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(Director,
     on_delete=models.CASCADE, related_name='movies')

    @property
    def rating(self):
        return self.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating'] or 0

    def __str__(self):
        return self.title



STARS = (
    (star, '*' * star) for star in range(1, 6)
)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
     related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)

