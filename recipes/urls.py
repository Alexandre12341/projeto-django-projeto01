from django.urls import path

from recipes.views import conto, home, sabre

urlpatterns = [
    path("", home),
]
