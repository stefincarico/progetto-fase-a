# blog/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post # Importiamo il nostro modello Post!
from django.shortcuts import redirect # Ci servirà per reindirizzare l'utente
from django.contrib import messages # Per mostrare messaggi di successo
from .forms import ContactForm, PostForm, UserRegisterForm
from django.contrib.auth.decorators import login_required # Importa il decorator!

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# -------------------------------------------------------------------
# QUESTA È LA NOSTRA NUOVA VIEW BASATA SU CLASSE
class PostListView(ListView):
    model = Post # 1. Quale modello interrogare
    template_name = 'blog/home.html' # 2. Quale template usare
    context_object_name = 'posts' # 3. Come si chiamerà la nostra lista nel template
    ordering = ['-date_posted'] # Aggiungiamo anche l'ordinamento
# -------------------------------------------------------------------


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def post_create(request):
    # Logica per creare un post (la vedremo dopo)
    return redirect('blog-home') # Per ora, reindirizziamo alla home

def about(request):
    # Non abbiamo ancora creato questo template, ma prepariamo la view
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    if request.method == 'POST':
        # Se il metodo è POST, l'utente ha inviato dei dati.
        # Creiamo un'istanza del form POPOLANDOLA con i dati dalla richiesta.
        form = ContactForm(request.POST)
        if form.is_valid():
            # is_valid() fa tutta la magia: validazione, pulizia...
            # Se i dati sono validi, li possiamo leggere da form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']

            # Qui, in un'app reale, invieremmo un'email.
            # Per ora, stampiamo solo in console.
            print(f"NUOVO MESSAGGIO DA {name} ({email}): {message_text}")
            
            messages.success(request, 'Il tuo messaggio è stato inviato con successo!')
            return redirect('blog-home') # Reindirizza l'utente alla home
    else:
        # Se il metodo è GET (o qualsiasi altro), l'utente ha appena visitato la pagina.
        # Creiamo un'istanza del form VUOTA.
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # Il template di default sarebbe post_form.html, che abbiamo già.
    
    # Dobbiamo sovrascrivere questo metodo per assegnare l'autore
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    # Django per convenzione cercherà <app>/<model>_detail.html
    # Quindi non serve specificare il template_name se seguiamo la convenzione.

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home') # Dove andare dopo la cancellazione
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Salva il nuovo utente nel database!
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creato per {username}! Ora puoi fare il login.')
            return redirect('login') # Reindirizza alla pagina di login
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

