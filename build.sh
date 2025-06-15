# Install Python dependencies
pip install -r requirements.txt

# Apply DB migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput