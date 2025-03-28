import os
# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Replace 'techwave' with your actual project name if different

# Setup Django
import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()


# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Replace 'techwave' with your actual project name if different

# Setup Django
django.setup()

users = User.objects.all()
print(f"Number of users found: {users.count()}")


for user in users:
    print(f"Username: {user.username}, Email: {user.email}, Last Login: {user.last_login}, Password: {user.password}")
