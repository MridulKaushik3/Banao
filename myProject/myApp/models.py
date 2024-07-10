from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to="picture")
    address=models.TextField()
    
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    user_type = models.CharField(
        max_length=7,
        choices=USER_TYPE_CHOICES,
        default='patient',
    )
    
    