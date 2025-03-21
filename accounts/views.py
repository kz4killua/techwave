from django.shortcuts import render, redirect
from django.contrib.auth import logout

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('catalog:item_list')
    else:
        return render(request, 'registration/logout.html')