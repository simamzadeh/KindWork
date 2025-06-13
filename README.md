# KindWork
Python web-based application, created for a university assignment. This application promotes being kind and positive with ourselves and to those around us.

## Prerequistes

- pip installed ([Link to install pip](https://pip.pypa.io/en/stable/installation/))

- python installed ([Link to install Python](https://www.python.org/downloads/))

- git installed ([Link to install git](https://github.com/git-guides/install-git))

The recommended IDE for running this programme is Visual Studio Code. Please make sure you are on a macOS, Windows or Linux machine. 


## Setting up your environment

1. Close the repository from git using:

`git clone https://github.com/simamzadeh/KindWork.git'

2. Create a virtual environment by running

`python -m venv venv`

3. Activate the environment

`source venv/bin/activate`

4. Install dependencies from the root folder

`pip install -r requirements.txt`

## Building the React package

1. Build React package by navigating to React project root

`cd kind_app/static/react/kind-app-react`

2. Run the build command.

`npm run build`

This will build the project and collect all React static files under static/. Django will pick these up from there and server them as front end.

3. To run the React app:

`npm run start`

## Building the Django package

1. To ensure all database migrations are applied, from the root project folder (KindApp/) run:

`python manage.py makemigrations`

and

`python manage.py migrate`

2. Now the application can be run locally using

`python manage.py runserver`

# Development instructions

1. To save installed dependencies, run this command from the project root folder

`pip freeze > requirements.txt`

2. Any changes made to code can be added and committed as normal

`git add -A` 

and 

`git commit -m "Commit message"`

3. Push the code with

`git push`

Render automatically registers new git commits and starts deploying them immediately.

Live URL here: https://kindwork.onrender.com/ 

# Local Testing

1. Ensure any React frontend changes have been built using the `npm run build` command from the React project root (`kind_app_react`)

2. From the Django root directory run `python manage.py runserver` to open the local development server.

> Make sure you've commented out throttling in the settings.py file before opening the server!