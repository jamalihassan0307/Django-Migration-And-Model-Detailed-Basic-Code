# Implementing Google Authentication in Django

This guide provides a detailed, step-by-step approach to implementing Google authentication in your Django application.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Google Cloud Console Account Setup](#google-cloud-console-account-setup)
3. [Project Setup](#project-setup)
4. [Google Cloud Console Configuration](#google-cloud-console-configuration)
5. [Django Configuration](#django-configuration)
6. [Implementation Steps](#implementation-steps)
7. [Testing](#testing)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

Before starting, ensure you have:
- Python 3.8+ installed
- Django 4.0+ installed
- A Google account (Gmail)
- Basic understanding of Django and OAuth2

## Google Cloud Console Account Setup

1. **Create a Google Cloud Account**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Click "Get Started" or "Sign In"
   - Sign in with your Google account
   - Accept the terms of service

2. **Create a New Project**
   - Click on the project dropdown at the top of the page
   - Click "New Project"
   - Enter a project name (e.g., "Django Google Auth")
   - Click "Create"
   - Wait for the project to be created
   - Note down your Project ID

3. **Enable Required APIs**
   - In the left sidebar, go to "APIs & Services" > "Library"
   - Search for "Google+ API" or "Google People API"
   - Click on the API
   - Click "Enable"
   - Wait for the API to be enabled

4. **Configure OAuth Consent Screen**
   - Go to "APIs & Services" > "OAuth consent screen"
   - Select "External" user type
   - Click "Create"
   - Fill in the required information:
     - App name: Your application name
     - User support email: Your email
     - Developer contact information: Your email
   - Click "Save and Continue"
   - Add scopes:
     - Click "Add or Remove Scopes"
     - Select:
       - `.../auth/userinfo.email`
       - `.../auth/userinfo.profile`
   - Click "Save and Continue"
   - Add test users:
     - Click "Add Users"
     - Add your email address
   - Click "Save and Continue"
   - Review your settings
   - Click "Back to Dashboard"

5. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Select "Web application" as the application type
   - Name: "Django Google Auth"
   - Add Authorized JavaScript origins:
     ```
     http://localhost:8000
     http://127.0.0.1:8000
     ```
   - Add Authorized redirect URIs:
     ```
     http://localhost:8000/social-auth/complete/google-oauth2/
     http://127.0.0.1:8000/social-auth/complete/google-oauth2/
     ```
   - Click "Create"
   - You will see a popup with your credentials:
     - Client ID
     - Client Secret
   - **IMPORTANT**: Copy and save these credentials securely
   - Click "OK"

6. **Verify Credentials**
   - Go back to "Credentials"
   - You should see your OAuth 2.0 Client ID listed
   - Click on it to view details
   - Verify that all URIs are correct
   - Note: Changes may take 5-10 minutes to propagate

## Project Setup

1. Install required packages:
```bash
pip install django social-auth-app-django
```

2. Add the following to your `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'myapp',
]
```

3. Add social auth middleware:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]
```

## Google Cloud Console Configuration

1. **Update Your Settings**
   - Open your Django project's `settings.py`
   - Add your credentials:
   ```python
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-client-id'  # From step 5
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-client-secret'  # From step 5
   ```

2. **Verify Configuration**
   - Make sure your project is selected in Google Cloud Console
   - Verify that the OAuth consent screen is configured
   - Check that the APIs are enabled
   - Confirm that your credentials are active

## Django Configuration

1. Add authentication backends in `settings.py`:
```python
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
```

2. Configure Google OAuth2 settings:
```python
# Google OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-client-secret'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'access_type': 'offline',
    'prompt': 'consent'
}
```

3. Set up redirect URLs:
```python
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
```

4. Configure social auth pipeline:
```python
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
```

## Implementation Steps

1. Create a login view in `views.py`:
```python
from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'login.html')
```

2. Create a login template (`login.html`):
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container-fluid {
            height: 100vh;
            background-color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container-fluid > div {
            width: 85%;
            min-width: 300px;
            max-width: 500px;
        }
        .card {
            width: 100%;
            background-color: #282c34;
            padding: 20px;
            border-radius: 8px;
        }
        .google-btn {
            background-color: #4285f4;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            display: inline-block;
            text-align: center;
            width: 100%;
            margin: 10px 0;
            transition: background-color 0.3s ease;
        }
        .google-btn:hover {
            background-color: #357abd;
        }
        .user-info {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container-fluid">
        <div>
            <h1 class="text-center mb-4">Sign in</h1>
            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}

            {% if user.is_authenticated %}
                <div class="user-info">
                    <h3>Welcome, {{ user.get_full_name|default:user.username }}!</h3>
                    <p><strong>Email:</strong> {{ user.email }}</p>
                    <p><strong>Username:</strong> {{ user.username }}</p>
                    <p><strong>Last Login:</strong> {{ user.last_login|date:"F j, Y, g:i a" }}</p>
                    <a href="{% url 'logout' %}" class="btn btn-danger">Logout</a>
                </div>
            {% else %}
                <div class="card">
                    <div class="row">
                        <div class="col-md-8 mx-auto social-container my-2">
                            <button class="google-btn">
                                <a href="{% url 'social:begin' 'google-oauth2' %}">
                                    Login With Google
                                </a>
                            </button>
                        </div>
                    </div>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
```

3. Add URLs in `urls.py`:
```python
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Testing

1. Start your Django development server:
```bash
python manage.py runserver
```

2. Visit `http://localhost:8000/login/`
3. Click the "Login with Google" button
4. Complete the Google authentication process
5. Verify that you're redirected back to the login page with your user information displayed

## Troubleshooting

Common issues and solutions:

1. **NoReverseMatch Error**
   - Ensure all URL patterns are properly defined
   - Check that template tags are correctly formatted

2. **Authentication Failed**
   - Verify Google Cloud Console credentials
   - Check redirect URIs match exactly
   - Ensure scopes are properly configured

3. **User Data Not Displaying**
   - Check if user is properly authenticated
   - Verify template context variables
   - Check social auth pipeline configuration

4. **Session Issues**
   - Clear browser cookies
   - Check session middleware configuration
   - Verify session settings in Django

## Security Considerations

1. Always use HTTPS in production
2. Keep your OAuth credentials secure
3. Implement proper session management
4. Add rate limiting for login attempts
5. Use secure cookie settings

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Social Auth Documentation](https://python-social-auth.readthedocs.io/)
- [Google OAuth2 Documentation](https://developers.google.com/identity/protocols/oauth2)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 