from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create a signup form fields
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username= forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')

# Create a profile update form fields
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','followers','following'] 
     
     
# Create a question form fields
class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
        # exclude = ['user','location'],
		fields = ['question_title', 'your_question', 'image_path','pub_date']


# Create a answer form fields
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['user','profile']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Explore
        exclude = ['user','profile']        
        

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ('post',)
#         exclude = ['user']

        		

