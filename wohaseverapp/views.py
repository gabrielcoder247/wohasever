from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

# Create your views here.



def signup(request):
    title = "signup"
    
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


@login_required(login_url='/accounts/login/')
def home(request):
    title = "Home"

    current_user = request.user
    question = Question.objects.filter(user=request.user) 
    answer = Answer.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'question' in request.POST:
            question_form = QuestionForm(request.POST,request.FILES,instance=request.user, prefix='questioned')
            if question_form.is_valid:
                question_form.save()
            question_form = QuestionForm(prefix='questioned')

        elif 'answer' in request.POST:
            answer_form = AnswerForm(request.POST,request.FILES,instance=request.user, prefix='answered')
            if answer_form.is_valid:
                answer_form.save()

    else:
            question_form = QuestionForm(prefix='questioned')
            answer_form = AnswerForm('answered')
            
    # if request.method == 'POST':
    #     question_form = QuestionForm(request.POST,request.FILES,instance=request.user)
    #     answer_form = AnswerForm(request.POST,request.FILES,instance=request.user)
       

    #     if question_form.is_valid or answer_form.is_valid:
    #         question_form.save()
    #         answer_form.save()

    #         return HttpResponseRedirect(reverse_lazy('home') )
   

    #     else:
    #         question_form = QuestionForm()
    #         answer_form = AnswerForm()

            
    return render(request, 'home.html', {"question_form": question_form,"answer_form": answer_form,
                                        "title":title, "current_user":current_user,"question":question,"answer":answer})




@login_required(login_url='/accounts/login/')
def search_results(request): 

    #query all username to find search_term  
    if 'question_title' in request.GET and request.GET["question_title"]:
        search_term =request.GET.get("question_title")
        search_title = Question.search_question(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_title})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message}) 

@login_required(login_url='/accounts/login/')
def search_category(request): 

    #search for  category in explore 
    if 'category' in request.GET and request.GET["category"]:
        search_term =request.GET.get("category")
        search_category = Question.search_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_category})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message}) 

@login_required(login_url='/accounts/login/')
def explore(request,id):
    category = Explore.get_category(category_id =id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            category.save()
            messages.success(request, ('You have created a category of your interest' ))
            return redirect('home')
            
    else:
        
        # messages.error(request, ('You have have not successfully signed up' )
        form = CategoryForm()




    return render(request, 'explore.html', {"category":category, "form":form})







  