from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = models.CharField(max_length =300)
    contact = models.CharField(max_length =30)  

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def __str__(self):
        return str(self.user)


