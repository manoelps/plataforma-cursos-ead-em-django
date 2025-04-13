from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_ead, name='home'),
]
