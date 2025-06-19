import logging
from django.shortcuts import render

logger = logging.getLogger('kind_app')

def lockout(request, credentials=None, *args, **kwargs):
    """
    View that handles account lockouts from django-axes
    """
    username = kwargs.get('username', '')
    if not username and credentials:
        username = credentials.get('username', '')
    
    logger.warning(f"Account locked due to too many failed login attempts: {username}")
    return render(request, 'account_locked.html')