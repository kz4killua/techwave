from django.apps import AppConfig  # Import Django's app configuration class

# Configuration class for the 'catalog' app
class CatalogConfig(AppConfig):
    # Defines the default auto-incrementing primary key type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specifies the name of the application
    name = 'catalog'
