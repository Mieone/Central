# Central
A Repository of Common services used by different applications in Mieone

Install GIT

Install python2.7

Install MYSQL

Install python-virtualenv

Do git clone: "git clone git@github.com:Mieone/Central.git"

cd clone dir

virtualenv Central

source CENTRAL/bin/activate

pip install -r requirements.pip

do the below changes(temporary issues)
CENTRAL/src/django-mailer/django_mailer/managers.py
line num 17, modify as "datetime.datetime.now()"

CENTRAL/src/django-mailer/django_mailer/management/commands/__init__.py
modify the index numbers("0", "1", "2") as integers(0, 1, 2)

Look into settings.py and Make some changes reg DB and debug...etc

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:
