from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.



def signup(request):
    title = signup
    
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username =username, password=raw_password)
            login(request, user)
            messages.success(request, ('You have been logged in' ))
            return redirect('home')
            
    else:
        
        # messages.error(request, ('You have have not successfully signed up' )
        form = SignUpForm()
        return render(request, 'signup.html', {"form":form})


def home(request):

    title = Home
    current_user = request.user
    question = Question.objects.filter(user=request.user) 
    answer = Answer.objects.filter(user=request.user) 

    if request.method == 'POST':
        question_form = QuestionForm(request.POST,request.FILES,instance=request.user)
        answer_form = AnswerForm(request.POST,request.FILES,instance=request.user)
        
        if question_form.is_valid or answer_form.is_valid:
            question_form.save()
            answer_form.save() 

    # elif request.method == 'POST':
    #     answer_form = AnswerForm(request.POST,request.FILES,instance=request.user)
    #     if answer_form.is_valid:
    #         answer_form.save() 

        else:
            question_form = ProfileForm()
            answer_form = ProfileForm()

            # return render(request, 'profile.html', {"image_form": image_form,"biz":biz,"profile":profile,"neighbour":neighbour,"pr":pr})
    return render(request, 'home.html', {"question_form": question_form,"answer_form": answer_form,
                                        'title':title, 'current_user':current_user,'question':question,'answer':answer})
  