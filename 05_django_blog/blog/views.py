# blog/views.py
from django.shortcuts import render
from .models import Post # Importiamo il nostro modello Post!

def home(request):
    # Usiamo l'ORM per prendere tutti gli oggetti Post dal database
    # e li ordiniamo per data, dal più recente al più vecchio.
    posts = Post.objects.all().order_by('-date_posted')

    # Creiamo un "contesto", un dizionario Python.
    # La chiave ('posts') sarà il nome della variabile che useremo nel template.
    # Il valore (posts) è il QuerySet che abbiamo appena creato.
    context = {
        'posts': posts
    }

    # Passiamo il contesto al template.
    # La funzione render si occuperà di rendere questa variabile
    # disponibile nel file HTML.
    return render(request, 'blog/home.html', context)

def about(request):
    # Non abbiamo ancora creato questo template, ma prepariamo la view
    return render(request, 'blog/about.html', {'title': 'About'})