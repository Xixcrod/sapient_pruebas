from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def dashboard(request):
    return render(request, 'core/dashboard.html')

def signin(request):
    return render(request, 'core/login.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))
