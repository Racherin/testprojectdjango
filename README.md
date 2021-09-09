pip install virtualenv

virtualenv venv

CMD:
venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver