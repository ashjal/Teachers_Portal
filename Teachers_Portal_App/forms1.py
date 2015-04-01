from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
	first_name=forms.CharField(label='First Name', max_length=40)
	last_name=forms.CharField(label='Last Name', max_length=40)
	designation=forms.CharField(label='Designation', max_length=20)
	username = forms.CharField(label='Username', max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password (Again)',widget=forms.PasswordInput())
	GENDER = ((1,("Male.")),(2,("Female.")),)
	Gender = forms.ChoiceField(choices=GENDER)
	DOB = forms.DateField(help_text="<em>YYYY-MM-DD</em>.")
	
def clean_password2(self):
	if 'password1' in self.cleaned_data:
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if password1 == password2:
			return password2
	raise forms.ValidationError('Passwords do not match.')
def clean_username(self):
	username = self.cleaned_data['username']
	if not re.search(r'^\w+$', username):
		raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
	try:
		User.objects.get(username=username)
	except ObjectDoesNotExist:
		return username
	raise forms.ValidationError('Username is already taken.')
