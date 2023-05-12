from django.db import models
from .models import *

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)
  

    def __str__(self):
        return self.first_name
    

class Blog(models.Model):
        cate = [ ('Fresh Vegetables', 'Fresh Vegetables'),
                  ('Farm Products', 'Farm Products'),
                   ('Fresh Fruits', 'Fresh Fruits'),
                    ('Organic Products', 'Organic Products'),
                      ('Organic Solution', 'Organic Solution')]
        discription  = models.CharField(max_length=150)
        name = models.TextField(max_length=100)
        
        pic = models.FileField(upload_to='blog_photo', default='health.jpeg')
        categories = models.CharField(max_length=150, choices=cate)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        time = models.DateTimeField(auto_now=True)

        def __str__(self) -> str:
            return self.name
        
class Comment(models.Model):
    message = models.CharField(max_length=150)
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
    
class Donation(models.Model):
    pay_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_to = models.ForeignKey(Blog, on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
