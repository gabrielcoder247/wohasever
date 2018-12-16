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

  


class Question(models.Model):
    title = models.CharField(max_length=100)
    your_question = models.TextField(max_length=300)
    pub_date = models.DateField(auto_now_add=False)
    image_path = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, related_name='user_question', blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
  


    @classmethod
    def get_all(cls):
        question = cls.objects.all()
        return question


    def save_question(self):
        self.save()


    def delete_question(self):
        self.delete()   
        
    @classmethod
    def search_question(cls, search_term):
        question = cls.objects.filter(title__icontains = search_term)
        return question
                
        

    class meta:
        ordering = ['-pub_date'] 



    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_answer')
    # image=models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='answer')
    your_answer = models.TextField(max_length=300,null=True)


    def get_Answer(self,id):
        answer= Answer.objects.filter(answer_id=id)
        return answer
        
    def save_answer(self):
        self.save()  

    @classmethod
    def search_answer(cls, search_term):
        answer = cls.objects.filter(title__icontains = search_term)
        return answer
                      

    def __str__(self):
        return self.title
    




class Explore(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    # image=models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    Category = models.CharField(max_length=50,null=True)
    search_category = models.CharField(max_length=50,null=True)
    created = models.DateField(auto_now_add=True)


    def get_category(self,id):
        category= Explore.objects.filter(category_id=id)
        return category
        
    def save_category(self):
        self.save()  

    @classmethod
    def search_category(cls, search_term):
        category = cls.objects.filter(category__icontains = search_term)
        return category
                      

    def __str__(self):
        return self.category

class Likes(models.Model):
    user = models.OneToOneField(User,related_name='user_likes')
    likes = models.IntegerField()

class Disikes(models.Model):
    user = models.OneToOneField(User,related_name='user_dislikes')
    dislikes = models.IntegerField()    

class Followers(models.Model):
    user = models.OneToOneField(User,related_name='user_followers')
    follower = models.CharField(max_length=20, default="")

class Followings(models.Model):
    user = models.OneToOneField(User,related_name='user_followings')
    following = models.CharField(max_length=20, default="")    