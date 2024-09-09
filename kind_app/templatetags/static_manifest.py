import json
import os

from django import template

register = template.Library()


@register.simple_tag
def get_manifest_file(file_name):
    manifest_path = os.path.join("kind_app/", "asset-manifest.json")

    if os.path.exists(manifest_path):
        with open(manifest_path) as manifest_file:
            manifest = json.load(manifest_file)
            files = manifest.get("files", {})
            resolved_path = files.get(file_name, file_name)
            return resolved_path
    return file_name