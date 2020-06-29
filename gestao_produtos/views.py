from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .forms import UserForm

# Create your views here.
def index(request):
    return redirect('produtos')

def logout_now(request):
    logout(request)
    return redirect('produtos')  

def sigin(request):
    form = UserForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    return render(request, 'registration/register.html', {'form': form})       