from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.http import JsonResponse

def check_authentication(request):
    # Return the current authentication status and username
    is_authenticated = request.user.is_authenticated
    username = request.user.username if is_authenticated else None
    return JsonResponse({'isAuthenticated': request.user.is_authenticated, 'username': username})

def logout_request(request):
    auth_logout(request)
    return render(request, "logout.html")
