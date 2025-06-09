
import json
import logging
import os

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import ensure_csrf_cookie

from kind.settings import DOMAIN

logger = logging.getLogger('kind_app')



# def index(request):
#     return HttpResponse("Hello, world. You're at the kind app index.")

# ===========================================================
# Utility functions and index
# ===========================================================
@ensure_csrf_cookie
def get_csrf_token(request):
    logger.debug(f"CSRF token requested by {request.META.get('REMOTE_ADDR')}")
    return JsonResponse({"success": "CSRF cookie set"})


def get_manifest(file_name):
    manifest_path = os.path.join("kind_app/", "asset-manifest.json")
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path) as manifest_file:
                manifest = json.load(manifest_file)
                files = manifest.get("files", {})
                result = files.get(file_name, file_name)
                logger.debug(f"Manifest lookup: {file_name} -> {result}")
                return result
        except Exception as e:
            logger.error(f"Error reading manifest: {str(e)}")
    logger.warning(f"Manifest not found or file {file_name} not in manifest")
    return file_name


def global_settings(request):
    return {
        "DOMAIN": DOMAIN,
    }


def index(request):
    logger.info(f"Index page accessed by {request.user.username if request.user.is_authenticated else 'anonymous'}")
    return render(request, "index.html")