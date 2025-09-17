
# blog/admin.py
from django.contrib import admin
from .models import Post # Importa il nostro modello Post

# Registra il modello Post nell'interfaccia di amministrazione
admin.site.register(Post)