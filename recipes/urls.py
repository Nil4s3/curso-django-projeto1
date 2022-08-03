from django.urls import path

from recipes.views import contato, home, sobre

# domain/recipes/
urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # about
    path('contato/', contato),  # contact

]
