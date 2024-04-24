# DjangoProjectRestaurant

DjangoProjectRestaurant is a web application developed using Django, a Python web framework. This project showcases a
restaurant website with features like menu management, table reservations, user reviews, and more.

# Installation

1. Clone the repository
   git clone https://github.com/<username>/<forked-repo>.git
2. Create your own virtual environment
   python3 -m venv venv
   source venv/bin/activate
3. Install your requirements
   pip install -r requirements.txt
4. Create a new PostgreSQL database
   For this, I’m assuming you already have pgAdmin and postgres installed. Apologies for the lack of detail here.

5. In your terminal:

$ psql postgres

$ CREATE DATABASE databasename

$ \connect databasename

Go into pgAdmin, login, and check that the new database exists on the dbserver.

The database credentials to go in your project’s settings.py are the same credentials for pgAdmin.

settings.py

DATABASES = {

‘default’: {

‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,

‘NAME’: env(‘DATABASE_NAME’),

‘USER’: env(‘DATABASE_USER’),

‘PASSWORD’: env(‘DATABASE_PASS’),

}

}

6. Generate a new secret key
   Use https://djecrety.ir/?source=post_page-----53d5939b7e9e-------------------------------- to quickly generate secure
   secret keys.
7. We also use a .env file to secure my secret key and database credentials. To find out more, check out my post on the
   topic.
8. Install Django Environ
In your terminal, inside the project directory, type:

$ pip install django-environ
9. Import environ in settings.py
import environ
10. Initialise environ
Below your import in settings.py:

import environ
Initialise environment variables
env = environ.Env()
environ.Env.read_env()
11. Create your .env file
In the same directory as settings.py, create a file called ‘.env’


12. Declare your environment variables in .env
Make sure you don’t use quotations around strings.

SECRET_KEY=SECRET_KEY
DATABASE_NAME=DB_NAME
DATABASE_USER=DB_USER
DATABASE_PASS=DB_PASS
13. IMPORTANT: Add your .env file to .gitignore
If you don’t have a .gitignore file already, create one at the project root.

Make sure the name of your .env file is included.

If you’re unsure what other file types belong in the .gitignore, visit this link for a sample.

14. Replace all references to your environment variables in settings.py
DATABASES = {
‘default’: {
‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
‘NAME’: env(‘DATABASE_NAME’),
‘USER’: env(‘DATABASE_USER’),
‘PASSWORD’: env(‘DATABASE_PASS’),
}
}
And

SECRET_KEY = env(‘SECRET_KEY’)

15. Rename the project
Rename the directory that contains settings.py. Do a find all and replace to rename all instances of the new project name.

16. Make your migrations
The only migrations that should appear in each of your app’s migrations folders are called ‘__init__.py’. As we have started a new database, we can delete any existing migrations and migrate from scratch.

In your terminal:

$ python manage.py makemigrations
$ python manage.py migrate
17. Create a new superuser
python manage.py createsuperuser
18. Final checks
Start the development server and ensure everything is running without errors.

python manage.py runserver
