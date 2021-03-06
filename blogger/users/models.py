from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default', upload_to='images')

    def __str__(self):
        return  '{} Profile'.format(self.user.username)