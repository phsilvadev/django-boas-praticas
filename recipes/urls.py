
from django.urls import path
from recipes.views import contatos, home, sobre  

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contatos/', contatos)
]
