
# Django Boilerplate with Simple JWT 🐍🔐

A simple Django project boilerplate that integrates DRF (Django Rest Framework) and **Simple JWT** for user authentication. This boilerplate provides a quick starting point for setting up JWT-based authentication and includes a user login API for your Django application. It uses PostgreSQL as the database. 🚀

## Features ✨

- JWT-based authentication with **Simple JWT** 🔑.
- User registration and login API 📝.
- Easy-to-extend structure for adding additional API endpoints ⚙️.
- Secure user authentication and session management 🔒.
- Uses PostgreSQL as the database 🗄️.

## Requirements ⚡

- Python 3.8 or higher 🐍
- Django 5.0.4 📦
- djangorestframework 3.15.1 📚
- python-dotenv 1.0.1 🌿
- psycopg2-binary 2.9.10 🍄
- djangorestframework-simplejwt 5.5.0 🔑

## Installation 🛠️

Follow these steps to get your Django project up and running:

### Create a Virtual Environment (optional but recommended) 🌱

First, create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies 📥


## Dependencies 📦

This project uses the following dependencies:

- **Django** – A high-level Python web framework.
- **Django REST Framework (DRF)** – A powerful toolkit for building Web APIs in Django.
- **Simple JWT** – A JSON Web Token authentication plugin for DRF.
- **PostgreSQL** – The database used by the project.

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

Make sure to have PostgreSQL running and configure your environment variables correctly.


Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Set Up PostgreSQL Database 🗄️

1. **Create a new PostgreSQL database for your project:**

   ```bash
   psql -U postgres
   CREATE DATABASE myproject_db;
   ```

2. **Update the `DATABASES` settings in your `settings.py` to use PostgreSQL:**

   ```python
   import os
   from dotenv import load_dotenv

   # Load environment variables from .env file
   load_dotenv()

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.getenv('DB_NAME'),
           'USER': os.getenv('DB_USER'),
           'PASSWORD': os.getenv('DB_PASSWORD'),
           'HOST': os.getenv('DB_HOST'),
           'PORT': os.getenv('DB_PORT'),
       }
   }
   ```

### Create a `.env` File 🌍

Create a `.env` file in the root of your project and add the following database credentials (these are sample values):

```env
DB_NAME=myproject_db
DB_USER=sample_user
DB_PASSWORD=sample_password
DB_HOST=localhost
DB_PORT=5432
```

This `.env` file will load into your Django settings, and the values will replace the `os.getenv()` calls in your `DATABASES` configuration.

### Set Up the Database 🔧

Run the following commands to create and migrate the database:

```bash
python manage.py migrate
```

### Create a Superuser (optional) 👑

If you'd like to access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### Start the Development Server 🚀

Run the following command to start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to see the app running.

## Usage 🔥

### Register a User 📝

To register a new user, send a **POST** request to `/api/auth/register/` with the following data:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```

### Login with JWT 🔑

To log in and get a JWT token, send a **POST** request to `/api/auth/login/` with the following data:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

You will receive a JWT token as a response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### Use the JWT Token for Authenticated Requests 🔓

To make authenticated requests, include the **access token** in the Authorization header:

```bash
Authorization: Bearer your_access_token
```

### Refresh JWT Token 🔄

To refresh your JWT token, send a **POST** request to `/api/auth/token/refresh/` with the following data:

```json
{
  "refresh": "your_refresh_token"
}
```

You will receive a new access token in the response.

## API Endpoints 📡

- **POST /api/auth/register/** – Register a new user.
- **POST /api/auth/login/** – Log in and get JWT tokens.
- **POST /api/auth/token/refresh/** – Refresh the access token using the refresh token.

## Settings ⚙️

You can configure JWT settings in the Django settings file (settings.py). The default settings should be sufficient for most use cases, but you can customize them according to your project’s needs.

## Development 💻

Feel free to fork this repository and extend it with your own features. You can add more API endpoints, custom models, or other functionality as required.

To contribute, please fork this repository, make your changes, and submit a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- Django
- Simple JWT

# License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
