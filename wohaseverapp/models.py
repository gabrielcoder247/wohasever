from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime as dt

# Create your models here.

class Profile(models.Model):

    pub_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name="profile")
    photo = models.ImageField(upload_to = 'profile/') 
    bio = models.TextField(max_length=255) 
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="followed_by", blank=True)


    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


    
    def get_following(self):
        users = self.following.all()
        return users.exclude


    def find_profile(cls,first_name):
        profile = Profile.objects.filter_by_name(name__icontains=first_name).all()
        return profile

    def get_following(self):
        users=self.following.all()
        return users.exclude(username = self.user.username)    


    def save_user(self):
         self.save()

    def delete_profile(self):
        self.delete()     
        
    @classmethod
    def get_all_profiles(cls):
        profile = cls.objects.all()
        return profile

    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0
     

    def __str__(self):
        return self.user.username

  

