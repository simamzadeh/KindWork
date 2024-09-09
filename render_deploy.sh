#!/bin/bash

# Exit script on any error
set -e

echo "===================================="
echo "Installing requirements..."
pip install -r requirements.txt

echo "===================================="
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "===================================="
echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "===================================="
echo "Success! Deploy script complete."