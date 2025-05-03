from django.urls import path
from . import views


urlpatterns = [
    path('ebook/', views.cheap_ebook, name="cheap-ebook")
]