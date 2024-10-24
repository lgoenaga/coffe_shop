from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def salir(request):
    logout (request)
    return redirect("login")