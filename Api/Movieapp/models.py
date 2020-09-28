from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100 , unique=True,blank=False)
    description=models.TextField(max_length=300,blank=False)

    def no_of_rating(self):
        ratings=Ratings.objects.filter(movie=self)
        return len(ratings)
    def avg_rating(self):
        sum=0
        ratings=Ratings.objects.filter(movie=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0
    def __str__(self):
        return self.title

class Ratings(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return self.movie
    class Meta:
        unique_together=(('user','movie'),)
        index_together=(('user','movie'),)
