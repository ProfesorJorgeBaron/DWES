from django.urls import path

from  .api_views import *

urlpatterns = [
    path('libros',libro_list)
]