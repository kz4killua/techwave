# Importing necessary modules from Django
from django.urls import path  # Used for defining URL patterns in the app
from django.contrib.auth import views as auth_views  # Importing built-in authentication views
from . import views  # Importing views from the current app (accounts)

# The app name to use for namespacing URLs in the 'accounts' app
app_name = 'accounts'

# URL patterns for the accounts app, mapping URLs to corresponding views
urlpatterns = [
    # URL for the login page, using Django's built-in LoginView
    # The template_name specifies the path to the login template to be used
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL for logging out the user, calling the custom signout view from the views module
    path('logout/', views.signout, name='logout'),
]
