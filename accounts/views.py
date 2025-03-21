# Importing necessary modules from Django
from django.shortcuts import render, redirect  # For rendering templates and redirecting users
from django.contrib.auth import logout  # Importing Django's built-in logout function

# View for handling user logout
def signout(request):
    # If the request method is POST (i.e., form submission for logout)
    if request.method == "POST":
        logout(request)  # Log the user out by calling Django's logout function
        return redirect('catalog:item_list')  # Redirect to the item list page (catalog:item_list) after logout
    else:
        # If not a POST request, render the logout confirmation page (i.e., a GET request)
        return render(request, 'registration/logout.html')  # Render the logout template
