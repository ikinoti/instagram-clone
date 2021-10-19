from cloudinary import CloudinaryImage
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  image = CloudinaryField('image', default='default.png')
  caption = models.TextField()
  created_date=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.caption
