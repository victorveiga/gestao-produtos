from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return redirect('produtos')

def logout_now(request):
    logout(request)
    return redirect('produtos')    