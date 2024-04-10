# CRUD
The CRUD project is a web application developed using Django, a Python web framework. Its primary purpose is to demonstrate the basic CRUD operations on a database. CRUD stands for Create, Read, Update, and Delete, which are essential functionalities in any database-driven application.
Introduction 

This CRUD (Create, Read, Update, Delete) project is built using Django, a high-level Python web framework. The purpose of this project is to demonstrate basic CRUD operations on a database through a web interface.

Features 

Create: Add new records to the database. 
Read: View existing records from the database. 
Update: Modify and update existing records. 
Delete: Remove records from the database.

Requirements 
Python 3.x 
Django 3.x 
Database (SQLite, MySQL, PostgreSQL, etc.)
Setup Clone the repository:
git clone https://github.com/sumitmishra672/CRUD 
cd Install dependencies:
Apply migrations to set up the database:
Copy code 
python manage.py migrate 
Create a superuser to access the Django admin:
Copy code 
python manage.py createsuperuser Run the development server:
Copy code 
python manage.py runserver 
Access the application at http://127.0.0.1:8000/.
Usage Admin Interface: 
Access the Django admin interface at http://127.0.0.1:8000/admin/ to manage database records. CRUD Operations: Use the application's web interface to perform CRUD operations on the database. Folder Structure /app: Contains the main Django application files. /templates: HTML templates for the application views. /static: Static files (CSS, JS, images, etc.) for the application. manage.py: Django's command-line utility for various tasks.
