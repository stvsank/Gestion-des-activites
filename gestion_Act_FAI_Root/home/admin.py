from django.contrib import admin
from .models import Employe, Conge, Client, Visite, Installation, Depannage, Retrait #import the Person model

# Register your models here.
admin.site.register(Employe)
admin.site.register(Conge)
admin.site.register(Client)
admin.site.register(Visite)
admin.site.register(Installation)
admin.site.register(Depannage)
admin.site.register(Retrait)
