from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='placeholder.jpg', upload_to='post_images')
    date_posted = models.DateTimeField(default=timezone.now)
    is_showcasing = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)


class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=60)
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    on_going = models.BooleanField(default=False)
