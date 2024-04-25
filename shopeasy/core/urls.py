from django.urls import path
from core import views
# from . import views = from core import views 

urlpatterns = [
    path('', views.index, name = 'index')
]