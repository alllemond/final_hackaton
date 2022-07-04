from django.db import models
from apps.movies.models import Movie   
from django.contrib.auth import get_user_model

User= get_user_model()

class Comment(models.Model):
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on the movie {self.movie}'



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    review = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like')
    like= models.BooleanField(default=False)


    def __str__(self):
        return str(self.like)

