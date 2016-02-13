# Central
A Repository of Common services used by different applications in Mieone

#Installation
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

#API_CALLS

SendSMS:

    --/api_call/sendsms/

      method: POST

      data: {"number": 1234567890, "message": "Hi ", "client_id": "FNVtgkQf7zrEaGyDUaS49j6I9c8AMyASHiZUB5M2", "client_secret": "nC4R9llmMIdPXWci9BvP2J2q9RT7hHtLKO439iW8Eng5Sqwjezgws8ItdLnJ8x8MWd0mGAarYSEL8a9BeVaihom3TEwswUflKJFotQiMhqbfWb3JbTbrhzaS4jtTShz7"}

      *Client_id : Contact administrator

      *Clent_secret: Contact administrator

Sendmail:
    --/api_calls/sendmail/
 
     method: POST

     data: {"to": mail_id, "message": "Hi ", "title": "Subject of Mail", "client_id": "FNVtgkQf7zrEaGyDUaS49j6I9c8AMyASHiZUB5M2", "client_secret": "nC4R9llmMIdPXWci9BvP2J2q9RT7hHtLKO439iW8Eng5Sqwjezgws8ItdLnJ8x8MWd0mGAarYSEL8a9BeVaihom3TEwswUflKJFotQiMhqbfWb3JbTbrhzaS4jtTShz7"}

      *Client_id : Contact administrator

      *Clent_secret: Contact administrator

