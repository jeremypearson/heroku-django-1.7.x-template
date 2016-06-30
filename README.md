# Heroku Django 1.7.x Template

>**WARNING: UNLESS YOU WANT TO MANUALLY MODIFY THE TEMPLATE BEFORE PROCESSING IT *(most of you I'd imagine would not want to do this)*, DO NOT *CLONE* THIS REPOSITORY AS IT CONTAINS A ```.env``` FILE WITH SETTINGS ONLY SUITABLE FOR LOCAL DEVELOPMENT. NEVER PUSH THIS REPOSITORY TO A PRODUCTION SERVER.**

>**A note about the above warning:** When I say "this repository", I am NOT referring to the repository that I tell YOU to create later on in the instructions of this ```README``` file which you would do by running the ```git init``` command after having run the ```django-admin.py startproject``` command among other commands that I tell you to run.

## Description
Inspired by: https://github.com/heroku/heroku-django-template and https://github.com/heroku/python-getting-started.
This is a basic Django 1.7.x Project Template, which contains only one Django Application. The project just displays the current date and time in UTC every time that the user loads the webpage.
The great thing about this Project Template, is that it's set up in a way that encourages the developer who uses it correctly to keep all of their secrets out of the source-code. It also encourages them to set DEBUG and DEBUG_TEMPLATES outside of the source-code. This is done through the use of environment variables.

Note: This Django Project Template has only been tested for Django 1.7.9. If you use another version Django 1.7.x and run into problems, please create 'issue' on the Github repository: https://github.com/jeremypearson/heroku-django-1.7.x-template

## Who this project is for
This project is for people who want to a) get a very simple database-driven Django Project containing a single Django App running locally on their machine where it will use either SQLite or PostgreSQL and b) who then want to successfully deploy that Django Project to Heroku where Heroku will use PostgreSQL.

Of course, once you have successfully deployed the Django Project to Heroku you'll probably want to start modifying it to do what YOU want it to do! You are not expected to release your modified version to the public domain just because you used this template which is in the public domain. Read the ```LICENSE``` file to learn more about what rights you have when using this template.

The instructions in this ```README``` file are for Mac OS X.

## Creating your project from the template
To use this Django Project Template, you should run this in your terminal (obviously replace ```name_of_your_project``` with the name that you want your project to have):
```
django-admin.py startproject --template=https://github.com/jeremypearson/heroku-django-1.7.x-template/archive/master.zip --name=Procfile name_of_your_project
```

## Running the Django project locally
Note: These instructions are specific to Mac OS X, if you have a different platform, they may need to be slightly adjusted.

### Pre-requisites
You have to already have installed and correctly configured all of the following:
* Python (https://www.python.org/downloads/)
* Pip (https://pip.pypa.io/en/latest/installing.html)
* Virtualenv (sudo pip install virtualenv)
* Virtualenvwrapper (sudo pip install virtualenvwrapper)
* Git (https://git-scm.com/downloads)
* Heroku Toolbelt (https://toolbelt.heroku.com)
* PostgreSQL (http://www.postgresql.org/download/) <-- If you have trouble installing this, read on for a possible workaround.

### What to do if you have trouble installing PostgreSQL
If you have trouble installing PostgreSQL on your local machine for some reason, AT THE POINT WHEN the instructions later on in this ```README``` file tell you to run the ```pip install -r requirements.txt``` command, run the following commands instead:
1. ```pip install dj-database-url==0.3.0```
1. ```pip install dj-static==0.0.6```
1. ```pip install Django==1.7.9```
1. ```pip install django-toolbelt==0.0.1```
1. ```pip install gunicorn==19.3.0```
1. ```pip install static3==0.6.1```
1. ```pip install wheel==0.24.0```
Doing that MIGHT solve your problem (I haven't actually tested this workaround, so I'm not sure that it would work. Let me know if it doesn't by creating an 'issue' for this repository on GitHub stating that this workaround doesn't work).

Note: While Heroku recommends that you use the same database in development as you do in production, you can choose not to. So you could just make the Django Project automatically use an SQLite database when it's running on your local machine, and automatically use a PostgreSQL database when it's running on Heroku.

### Instructions
#### Running the Django Project on your local machine, initially using the SQLite database backend.
1. Change into the directory that will hold the directory of the Django Project. For example: ```cd ~/dev/```
1. Create a virtualenv for it: ```mkvirtualenv name_of_your_project```
1. Install Django 1.7.9: ```pip install django==1.7.9```
1. Create a project using the project template: ```django-admin.py startproject --template=https://github.com/jeremypearson/heroku-django-1.7.x-template/archive/master.zip --name=Procfile name_of_your_project```
1. Change into the directory of the project you just created, for example: ```cd ~/dev/name_of_your_project```
1. Set this directory as the project directory of the virtualenv: ```setvirtualenvproject```
1. Install the project's dependencies: ```pip install -r requirements.txt```
1. Optionally change the following environment variables, within the ```.env``` file to the values you want for your local machine: ```SECRET_KEY```, ```DEBUG```, ```TEMPLATE_DEBUG```, ```PYTHONUNBUFFERED```. See section [The .env file](#the-env-file) for more information.
1. Source the ```.env``` file, so that the environment variables will exist when we run ```manage.py``` later on: ```source .env```
1. Make migrations: ```python manage.py makemigrations```
1. Apply migrations: ```python manage.py migrate```
1. Run the Django Project using ```foreman``` (```foreman``` is a part of the Heroku Toolbelt): ```foreman start```
1. Visit the project in your web browser at: http://localhost:5000, you should see the current date and time in UTC displayed every time you load the webpage.
1. You can stop running the server by hitting Ctrl+C (not Command+C) in the terminal that foreman is running in.

#### Running the Django Application on your local machine, using a PostgreSQL database backend, after you've successfully completed all of the instructions above
1. Create your PostgreSQL database which will only exist on your local machine for development. For example:
   1. Create new user for database (optional) (replace ```jeremy``` with the name of the user on your operating system which is displayed directly to the left of the ```$``` sign in your Terminal: ```createuser -U jeremy -deEP app_dateAndTime```
   1. Enter in password, such as: ```myPassword```
   1. Enter in that same password again, such as: ```myPassword```
   1. Create new database owned by a particular user (such as the user just created): ```createdb -e -E UTF8 -h localhost -U app_dateAndTime app_dateAndTime```
   1. Run psql: ```psql```
   1. View the list of databases to see the newly created database: ```\l```
   1. Hit the ```q``` key to quit reading it.
   1. Exit psql: ```\q```
1. Change the ```DATABASE_URL``` environment variable in the ```.env``` file to the appropriate value using the format: ```scheme://user:password@host:port/database```, for example: ```export DATABASE_URL='postgres://app_dateAndTime:myPassword@localhost:5432/app_dateAndTime'```
1. Source the ```.env``` file, so that the environment variables will exist when we run ```manage.py``` later on: ```source .env```
1. Make migrations: ```python manage.py makemigrations```
1. Apply the migrations: ```python manage.py migrate```
1. Run the Django Project using ```foreman```: ```foreman start```
1. Visit the project in your web browser at: http://localhost:5000, you should see the current date and time in UTC displayed every time you load the webpage.
1. You can stop running the server by hitting Ctrl+C (not Command+C) in the terminal that foreman is running in.

## Further modifying the .env file (optional)

The ```.env``` file is a file that contains environment variables that will **only be used on your local machine during development**. **Never put this file under source-control of your project**. It's useful to set the environment variable called "PYTHONUNBUFFERED" to true, as this will make the terminal display any strings printed by the Django Project, when you're running it using ```foreman```.

### Example of .env file's contents

```
# DEBUG is a required environment variable.
export DEBUG=true
# TEMPLATE_DEBUG is a required environment variable.
export TEMPLATE_DEBUG=true

######## DATABASE_URL is a required environment variable. ########

# Option 1. In this case settings.py would find and set the 'NAME' of the database, i.e. the absolute path of the database file.
export DATABASE_URL='sqlite'

# Option 2. In this case settings.py would find and set the 'NAME' of the database, i.e. the absolute path of the database file. This is equivalent to Option 1.
export DATABASE_URL='sqlite://'

# Option 3. In this case, the 'NAME' of the database will be set to the absolute path that's specified in this string. Replace the absolute path with your own.
export DATABASE_URL='sqlite:////Users/jeremy/dev/heroku_django_1_7_9_starter/db.sqlite3'

# Option 4. In this case a PostgreSQL database engine will be used. Change the components of the string to what you need.
export DATABASE_URL='postgres://app_dateAndTime:myPassword@localhost:5432/app_dateAndTime'
##################################################################

# PYTHONUNBUFFERED is an optional environment variable. It determines whether or not output from print statements in the Django project will be displayed in the console when running the Django project using foreman.
export PYTHONUNBUFFERED=true
```

## Deploying the app to Heroku
1. At this point, you'll probably want to delete the ```LICENSE``` file that came with this template, in your Django Project's directory, unless of course you want your project to be in the public domain.
1. Initiate the git repository: ```git init```
1. Add all directories and files that aren't set in ```.gitignore``` to be ignored: ```git add .```
1. Modify the ```runtime.txt``` file so that the Python Runtime specified in it is the one that you would like Heroku to use when it runs your Heroku Application. Visit here for more information: https://devcenter.heroku.com/articles/python-runtimes
1. Commit the initial project: ```git commit -m "Initial production-ready project."```
1. Log into heroku: ```heroku login```
1. Create your Heroku Application: ```heroku create your-heroku-app-name```
1. Create a PostgreSQL database on Heroku: ```heroku addons:create heroku-postgresql:hobby-dev```
1. Set your production ```SECRET_KEY``` environment variable (make this **unique** and **strong**): ```heroku config:set SECRET_KEY='YOUR_SUPER_SECRET_SUPER_STRONG_UNIQUE_PRODUCTION_SECRET_KEY'```
1. Set your production ```DEBUG``` environment variable (**ensure this is set to false**): ```heroku config:set DEBUG=false```
1. Set your production ```TEMPLATE_DEBUG``` environment variable (**ensure this is set to false**): ```heroku config:set TEMPLATE_DEBUG=false```
1. Deploy your Django Project to Heroku: ```git push heroku master```
1. Apply migrations to PostgreSQL database on Heroku: ```heroku run python manage.py migrate```
1. Visit the project in your web browser at: http://your-heroku-app-name.herokuapp.com, you should see the current date and time in UTC displayed every time you load the webpage.
1. If the app isn't running on Heroku, then you might need manually scale it to use 1 dyno: ```heroku ps:scale worker=1```
