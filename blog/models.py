from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    likes=models.ManyToManyField(User,related_name='likes')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
