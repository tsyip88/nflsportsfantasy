from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    date_time = models.DateTimeField()
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)