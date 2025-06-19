import ipaddress
import socket
from urllib.parse import urlparse
from django.core.exceptions import PermissionDenied
import logging

logger = logging.getLogger('kind_app')

class SSRFProtectionMiddleware:
    """
    SSRF Protection Middleware - Prevents Server Side Request Forgery attacks
    by blocking requests to internal/private networks.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        # Block common private IP ranges to prevent SSRF
        self.private_ranges = [
            '127.0.0.0/8',      # Localhost
            '10.0.0.0/8',       # Private network
            '172.16.0.0/12',    # Private network
            '192.168.0.0/16',   # Private network
            '169.254.0.0/16',   # Link-local
            '::1/128',          # Localhost IPv6
            'fc00::/7',         # Private IPv6
        ]

    def __call__(self, request):
        # Check request for potential SSRF attempts
        self._check_request_for_ssrf(request)
        return self.get_response(request)

    def _check_request_for_ssrf(self, request):
        # Check URL parameters in GET and POST requests
        for key, value in request.GET.items():
            if self._is_url(value) and not self._is_safe_url(value):
                logger.warning(f"SSRF attempt blocked in GET: {key}={value}")
                raise PermissionDenied("SSRF attempt blocked")
        
        if request.method == 'POST':
            for key, value in request.POST.items():
                if self._is_url(value) and not self._is_safe_url(value):
                    logger.warning(f"SSRF attempt blocked in POST: {key}={value}")
                    raise PermissionDenied("SSRF attempt blocked")

    def _is_url(self, value):
        # Simple check if a string looks like a URL
        if not isinstance(value, str):
            return False
        return value.startswith(('http://', 'https://', '//'))

    def _is_safe_url(self, url):
        # Verify URL doesn't resolve to private/internal IP
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        
        if not hostname:
            return True
            
        try:
            # Resolve hostname to IP and check against private ranges
            ip_address = socket.gethostbyname(hostname)
            ip = ipaddress.ip_address(ip_address)
            
            for private_range in self.private_ranges:
                if ip in ipaddress.ip_network(private_range):
                    return False
                    
            return True
        except (socket.gaierror, ValueError):
            # If hostname can't be resolved, block it to be safe
            return False