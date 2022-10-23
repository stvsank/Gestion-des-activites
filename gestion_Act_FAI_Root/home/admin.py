from django.contrib import admin
from .models import Employe, Conge #import the Person model

# Register your models here.
admin.site.register(Employe)
admin.site.register(Conge)
