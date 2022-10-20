from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.userSpace, name='userSpace'),
    path('historique/', views.historique, name='historique'),
    path('info/<int:id>', views.infoActEmploy, name='infoActEmploy'),
]