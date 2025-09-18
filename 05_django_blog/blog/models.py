# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Importiamo il modello Utente di Django

# Ogni classe Model corrisponde a una tabella nel database
from django.urls import reverse


class Post(models.Model):
    # ... (i tuoi campi title, content, etc. restano qui)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Restituisce l'URL canonico per un'istanza di questo modello."""
        # reverse() costruisce un URL a partire dal nome definito in urls.py
        # kwargs passa i parametri richiesti dall'URL (in questo caso, la chiave primaria del post)
        return reverse('post-detail', kwargs={'pk': self.pk})
