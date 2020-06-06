from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('adddojo', views.addDojo),
    path('addninja', views.addNinja),
    path('removedojo/<int:removeid>', views.removeDojo),
]