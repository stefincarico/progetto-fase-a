# blog/urls.py
from django.urls import path
# Importiamo direttamente la nostra nuova classe
from .views import PostCreateView, PostDeleteView, PostListView, PostDetailView, PostUpdateView
from . import views

# Questo file gestisce gli URL specifici dell'app 'blog'
urlpatterns = [
    # La vecchia riga era: path('', views.home, name='blog-home'),
    # La nuova riga è:
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
