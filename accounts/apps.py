from django.apps import AppConfig

class AccountsConfig(AppConfig):
    # Specifies the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Defines the name of the application, which should match the app directory name
    name = 'accounts'