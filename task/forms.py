from django import forms

def widget_attrs(placeholder):
	return {'class': 'form-control mb-2 mr-md-2', 'placeholder':placeholder}

def form_kwargs(widget, label, max_length):
	return {'widget':widget, 'label': label, 'max_length': max_length}

class TaskListForm(forms.Form):
	title = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Start a new list of tasks')),
			label='',
			max_length=20
			)
		)

class TaskForm(forms.Form):
	description = forms.CharField(
		**form_kwargs(
			widget = forms.TextInput(attrs=widget_attrs('Describe your tasks here')),
			label='',
			max_length=255
			)
		)
