# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")  # Redirect to login page
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('catalog:item_list')
    return render(request, 'registration/logout.html')