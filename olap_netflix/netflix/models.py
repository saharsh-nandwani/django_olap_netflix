from django.db import models

# Create your models here.

class popularPlan(models.Model):
    user_id = models.IntegerField()
    plan_name=models.CharField(max_length=255)
    plan_id = models.IntegerField()
    payment_id = models.IntegerField()

class trendingMovies(models.Model):
    count = models.IntegerField()
    rating = models.IntegerField()
    movie_id=models.IntegerField()

class languageCountry(models.Model):
    user_country = models.CharField(max_length=255)
    language_id = models.IntegerField()
