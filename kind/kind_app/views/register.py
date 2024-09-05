from django.shortcuts import  render, redirect
from kind_app.forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import *
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"register_form":form})
