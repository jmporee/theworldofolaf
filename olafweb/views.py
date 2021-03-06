from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import LoginForm

# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)
    
def date_actuelle(request):
    return render(request, 'olafweb/date.html', {'date': datetime.now()})
    
def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2
    return render(request, 'olafweb/addition.html', locals())
    
def login(request):
    form = LoginForm()
    return render_to_response ('olafweb/login.html', {'form': form})
  # Le formulaire n'a pas été envoyé
  