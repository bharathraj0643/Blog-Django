#!/bin/bash

echo "📦 Installing requirements..."
pip install -r requirements.txt

echo "🧼 Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

echo "🗃️ Applying DB migrations..."
python manage.py migrate --noinput

echo "📁 Listing contents of $(pwd):"
ls -al

echo "📁 Listing staticfiles:"
ls -al staticfiles/