from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=25, null=False, blank= False)

    topic = models.CharField(max_length=25, null=False, blank=False)

    content = models.TextField()

    image = models.ImageField(default="fallback.png", upload_to="post-images", blank=True)

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class Subscriber(models.Model):
        
    city_choices = [
        ('Nairobi','Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Machakos','Machakos'),
        ('Kisumu','Kisumu'),
        ('Kiambu','Kiambu'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Lamu', 'Lamu'),
        ('Thika', 'Thika'),
    ]
        

    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    email = models.EmailField(null=True, blank=True)

    phone = models.CharField(max_length=25)

    subscriber_residence = models.CharField(max_length=50, choices=city_choices, blank=True, null=True)

    joined_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):

        return self.first_name + "   " + self.last_name