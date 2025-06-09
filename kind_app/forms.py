import logging
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

logger = logging.getLogger('kind_app')

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		
	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		logger.debug(f"Validating registration form for username: {username}, email: {email}")
		return cleaned_data

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		logger.info(f"Registration form saving user: {user.username}, email: {user.email}")
		if commit:
			user.save()
			logger.info(f"User {user.username} saved to database")
		else:
			logger.debug(f"User {user.username} created but not saved to database (commit=False)")
		return user