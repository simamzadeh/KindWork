import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from axes.decorators import axes_dispatch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

logger = logging.getLogger('kind_app')

@axes_dispatch
@never_cache
def login_request(request):
	logger.info(f"Login page accessed. Method: {request.method}")
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request=request, username=username, password=password)
			if user is not None:
				login(request, user)
				logger.info(f"User '{username}' logged in successfully")
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				logger.warning(f"Failed login attempt for username: {username}")
				messages.error(request,"Invalid username or password.")
		else:
			logger.warning(f"Invalid login form submission: {form.errors}")
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", {"login_form":form})