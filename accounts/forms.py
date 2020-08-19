from django import forms
from django.contrib.auth.models import User

def widget_attrs(placeholder):
	return {'class': 'form-control mb-2 mr-md-2', 'placeholder':placeholder}

def form_kwargs(widget, label, max_length):
	return {'widget':widget, 'label': label, 'max_length': max_length}

class RegistrationForm(forms.Form):
	first_name = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('First name')),
			label = '',
			max_length = 20
		)
	)
	last_name = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Last name')),
			label = '',
			max_length = 20
		)
	)
	username = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Username')),
			label = '',
			max_length = 15
			)
		)

	email = forms.EmailField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Email')),
			label = '',
			max_length = 64 + 255
			)
		)

	password = forms.CharField(
		**form_kwargs(
			widget = forms.PasswordInput(attrs=widget_attrs('Password')),
			label = '',
			max_length = 64
			)
		)

	password_confirmation = forms.CharField(
		**form_kwargs(
			widget = forms.PasswordInput(attrs=widget_attrs('Confirm Password')),
			label = '',
			max_length = 64
			)
		)

	def clean(self):
		password = self.cleaned_data.get('password')
		password_confirmation = self.cleaned_data.get('password_confirmation')

		if password != password_confirmation:
			raise forms.ValidationError('Passwords do not match!')

		return self.cleaned_data

class LoginForm(forms.Form):
		username = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Username')),
			label = '',
			max_length = 15
			)
		)

		password = forms.CharField(
		**form_kwargs(
			widget = forms.PasswordInput(attrs=widget_attrs('Password')),
			label = '',
			max_length = 64
			)
		)

		def clean(self):
			username = self.cleaned_data.get('username')
			password = self.cleaned_data.get('password')
			user = User.objects.filter(username=username).first()

			if not user:
				raise forms.ValidationError('Username not registered!')

			elif user and not user.check_password(password):
				raise forms.ValidationError('Password Incorrect!')

			return self.cleaned_data

class ProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

	def clean(self):
		username = self.cleaned_data.get('username')
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
		
		return self.cleaned_data
		