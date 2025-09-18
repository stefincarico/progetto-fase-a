# blog/forms.py
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Il tuo Nome")
    email = forms.EmailField(label="La tua Email")
    message = forms.CharField(widget=forms.Textarea, label="Messaggio")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Aggiungiamo un campo email

    class Meta:
        model = User
        fields = ['username', 'email'] # Definiamo i campi che vogliamo