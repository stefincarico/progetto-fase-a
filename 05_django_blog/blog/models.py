# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Importiamo il modello Utente di Django

# Ogni classe Model corrisponde a una tabella nel database
class Post(models.Model):
    # Ogni attributo corrisponde a una colonna della tabella
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    # auto_now_add=True dice a Django di salvare la data e ora correnti
    # solo la prima volta che l'oggetto viene creato.
    date_posted = models.DateTimeField(default=timezone.now)
    # ForeignKey crea una relazione "molti-a-uno". Molti post possono
    # appartenere a un solo utente. on_delete=models.CASCADE dice a Django:
    # "se l'utente viene cancellato, cancella anche tutti i suoi post".
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title