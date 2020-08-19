from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import RegistrationForm, LoginForm, ProfileForm

# Create your views here.
def register(request):
	logout(request)
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			User.objects.create_user(
				first_name=request.POST['first_name'],
				last_name=request.POST['last_name'],
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
					messages.success(request, f'Welcome, {user.first_name}!')
					return redirect('task:task_list')
		else:
			return render(request, 'accounts/login.html', {'form':form})
	else:
		return render(request, 'accounts/login.html', {'form':LoginForm()})
	return redirect('accounts:login')

def logout_view(request):
	logout(request)
	return redirect('task:index')

@login_required(login_url='/auth/login/')
def profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Profile has been Updated!')
			return redirect('accounts:profile')
	else:
		form = ProfileForm(instance=request.user)

	return render(request, 'accounts/profile.html', {'form':form})
