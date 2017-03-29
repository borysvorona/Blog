from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE)
    category = models.ForeignKey('Category')
    title = models.TextField(unique=True)
    summary = models.TextField(default='summary')
    text = models.TextField()
    minute_read = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.email

class Category(models.Model):
    title = models.TextField(max_length=50, unique=True)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    main = models.BooleanField(default=False)
    about = models.TextField(default='Info about author')
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.surname