from django.urls import path

from recipes.views import home

# domain/recipes/
urlpatterns = [
    path('', home),  # home


]