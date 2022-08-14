from django.urls import path
from . import views

app_name = 'PharmaSales'
urlpatterns = [
    path('calculation/<str:year>/<str:data>', views.calculation, name='calculation')


]