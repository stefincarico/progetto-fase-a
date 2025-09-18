# blog/forms.py
from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Il tuo Nome")
    email = forms.EmailField(label="La tua Email")
    message = forms.CharField(widget=forms.Textarea, label="Messaggio")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']