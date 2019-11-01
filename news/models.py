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


class Neighborhood(models.Model):
    neigborhood_name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupants = models.IntegerField(default = 0, null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)

    @classmethod
    def create_neigborhood(cls):
        hoods = cls.objects.all()
        return hoods

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def update_neigborhood(cls,id,value):
        cls.objects.filter(id = id).update(neigborhood_name = new_hood)

    @classmethod
    def get_neigborhood_by_id(cls,id):
        neigborhood = cls.objects.filter(id = id).all()
        return neigborhood

    @classmethod
    def update_occupants(cls,id,value):
        cls.objects.filter(id = id).update(occupants = new_occupant)

    def __str__(self):
        return self.neigborhood_name