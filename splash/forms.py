from django.db import models
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from models import Entry
from django import forms


email_errors = {
    'required': 'Hi there! Please provide an email address.',
    'invalid': 'Hi! I\'m sorry, my limited machine brain was not able to validate your email address. Please verify it and use another one if it still doesn\'t work. Thanks!',
}

class EntryForm(ModelForm):
	problem = forms.CharField(widget=forms.Textarea(attrs={'name': 'editor1', 'style': 'height: 100px;' 'width:500px;'}))
	email = forms.EmailField(required=True, error_messages=email_errors)
	
	class Meta:
		model = Entry
		
		