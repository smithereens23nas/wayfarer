from audioop import reverse
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=500)
    description = models.TextField(max_length=500)

class Post(models.Model):
    title = models.CharField(max_length=100)
    city_id = models.ManyToManyField(City)
    img = models.TextField(max_length=500, blank =True)
    body = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('profile_detail', args=(str(self.id)))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    profile_picture = models.TextField(max_length=500, default ='https://i.pinimg.com/736x/cb/45/72/cb4572f19ab7505d552206ed5dfb3739.jpg')
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
