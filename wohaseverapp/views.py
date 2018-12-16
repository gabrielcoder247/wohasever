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
        messages.error(request, ('You have have not successfully signed up' ))
		form = SignUpForm()
	return render(request, 'signup.html', {"form":form})