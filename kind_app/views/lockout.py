import logging
from django.shortcuts import render

logger = logging.getLogger('kind_app')

def lockout(request, credentials, *args, **kwargs):
    """
    View that handles account lockouts from django-axes
    """
    logger.warning(f"Account locked due to too many failed login attempts: {credentials}")
    return render(request, 'account_locked.html')