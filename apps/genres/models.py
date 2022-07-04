from django.db import models
from slugify import slugify


class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,primary_key=True, blank=True)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug= slugify(self.title)
       super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = 'Genres'
