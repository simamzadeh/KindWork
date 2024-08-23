
import json
import os


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from django.views.decorators.csrf import ensure_csrf_cookie


from kind.settings import DOMAIN



# def index(request):
#     return HttpResponse("Hello, world. You're at the kind app index.")

# ===========================================================
# Utility functions and index
# ===========================================================
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"success": "CSRF cookie set"})


def get_manifest(file_name):
    manifest_path = os.path.join("kind_app/", "asset-manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path) as manifest_file:
            manifest = json.load(manifest_file)
            files = manifest.get("files", {})
            return files.get(file_name, file_name)
    return file_name


def global_settings(request):
    return {
        "DOMAIN": DOMAIN,
    }


def index(request):
    return render(request, "index.html")