from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import ultima_tesis_carreras
from django.contrib.auth.decorators import login_required
from .decorators import login_excluded

# Create your views here.
def dashboard(request):
    ultima_tesis_por_carrera = ultima_tesis_carreras.obtener_ultimas_tesis_por_carrera()
    return render(request, 'core/dashboard.html', {'ultima_tesis_carrera': ultima_tesis_por_carrera})

@login_excluded('dashboard')
def signin(request):
    return render(request, 'core/login.html')

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))
