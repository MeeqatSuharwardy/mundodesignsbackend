web: gunicorn ecommerce_project.wsgi -log-file- --log-level debug
python manage.py collectstatic --noinput
heroku ps:scale web=1
manage.py migrate
