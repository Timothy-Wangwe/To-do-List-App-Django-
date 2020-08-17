from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.forms import RegistrationForm, LoginForm

# Create your views here.
def register(request):
	logout(request)
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			User.objects.create_user(
				username=request.POST['username'],
				email=request.POST['email'],
				password=request.POST['password'],
				)
			messages.success(request, 'Account has been created! Please login below...')
			return redirect('accounts:login')
		else:
			return render(request, 'accounts/register.html', {'form':form})
	else:
		return render(request, 'accounts/register.html', {'form': RegistrationForm()})

def login_view(request):
	logout(request)
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				username=request.POST['username'],
				password=request.POST['password'],
				)
			if user is not None:
				if user.is_active:
					login(request, user)
					messages.success(request, f'Welcome, {user.username}!')
					return redirect('task:task_list')
		else:
			return render(request, 'accounts/login.html', {'form':form})
	else:
		return render(request, 'accounts/login.html', {'form':LoginForm()})
	return redirect('accounts:login')

def logout_view(request):
	logout(request)
	return redirect('task:index')
