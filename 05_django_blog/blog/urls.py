# blog/urls.py
from django.urls import path
from . import views # Importiamo le views dalla stessa cartella

urlpatterns = [
    # Quando l'utente visita l'URL "radice" dell'app (es. /blog/),
    # Django chiamerà la funzione 'home' che si trova in views.py.
    path('', views.home, name='blog-home'),
    
    # Questa nuova regola dice: l'indirizzo 'about/' va alla view 'about'
    path('about/', views.about, name='blog-about'),
]