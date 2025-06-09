import logging
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.http import JsonResponse

logger = logging.getLogger('kind_app')

def check_authentication(request):
    # Return the current authentication status and username
    is_authenticated = request.user.is_authenticated
    username = request.user.username if is_authenticated else None
    logger.debug(f"Authentication check: User {username if username else 'anonymous'} is {'authenticated' if is_authenticated else 'not authenticated'}")
    return JsonResponse({'isAuthenticated': request.user.is_authenticated, 'username': username})

def logout_request(request):
    username = request.user.username if request.user.is_authenticated else "anonymous"
    logger.info(f"User '{username}' logged out")
    auth_logout(request)
    return render(request, "logout.html")
