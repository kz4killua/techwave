# Importing necessary module from Django
from django.apps import AppConfig  # Used to configure application settings

# The AccountsConfig class configures the 'accounts' app within the project
class AccountsConfig(AppConfig):
    # Specifies the default primary key field type for models in this app
    # BigAutoField is used to generate large auto-incrementing integer values for primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # Defines the name of the application, which should match the app directory name
    # The app name 'accounts' should correspond to the directory in your project structure
    name = 'accounts'
