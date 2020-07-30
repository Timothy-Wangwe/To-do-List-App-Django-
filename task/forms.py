from django import forms

def widget_attrs(placeholder):
	return {'class': 'form-control mb-2 mr-md-2', 'placeholder':placeholder}

def form_kwargs(widget, label, max_length):
	return {'widget':widget, 'label': label, 'max_length': max_length}

