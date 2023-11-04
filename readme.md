# Initial steps of the Project

## Step 1
### Create a Virtual Environment
```bash
python -m venv .venv
```
### Activate the Virtual Environment
```bash
.\.venv\Scripts\activate
```
### Make a `.gitignore` file to prevent files getting a Git Commit
```bash
# Virtual Environment
.venv
```

## Step 2
### Install Required Libraries
```bash
pip install django
pip install requests
pip install python-dotenv
```
### Record environment's current package list
```bash
pip freeze > requirements.txt
```

## Step 3
### Create a Django project and app
```bash
django-admin startproject weather_project
cd weather_project
python manage.py startapp weather_app
``````

# Final step of the Project

### Run the Project
```bash
python manage.py runserver
```