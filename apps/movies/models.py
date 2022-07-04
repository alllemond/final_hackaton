
from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from apps.genres.models import Genre  

User = get_user_model()


class Movie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pub', verbose_name='Автор')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    year = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='film_genre', null=True)
    country = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='Images')


    def __str__(self):
        return f'{self.title} in {self.year}'

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name='Movie'
        verbose_name_plural= 'Movies'
        ordering = ['-year']   

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='movie_images')
    image = models.ImageField(upload_to='movie_images')

    def __str__(self):
        return self.movie


class Favorites(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.like)