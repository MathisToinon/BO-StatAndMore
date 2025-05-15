from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, "dashboard.html")

def comparaison(request):
    return render(request, "comparaison.html")

def secteur(request):
    return render(request, "secteur.html")

def carte(request):
    return render(request, "carte.html")