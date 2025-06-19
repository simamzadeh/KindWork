import logging
from django.shortcuts import  render, redirect
from kind_app.forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import *
from django.contrib import messages

logger = logging.getLogger('kind_app')

def sign_up(request):
    logger.info(f"Registration page accessed. Method: {request.method}")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Pass the request to authenticate the user first
            user = authenticate(request=request, username=user.username, password=form.cleaned_data.get('password1'))
            login(request, user)
            logger.info(f"New user registered: {user.username}")
            messages.success(request, "Registration successful." )
            return redirect("/")
        logger.warning(f"Failed registration attempt: {form.errors}")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"register_form":form})
