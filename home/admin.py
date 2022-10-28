from django.contrib import admin
from .models import Employe, Conge, Client, Visite, Installation, Depannage, Retrait, Routeur, Antenne

# Register your models here.
admin.site.register(Employe)
admin.site.register(Conge)
admin.site.register(Client)
admin.site.register(Visite)
admin.site.register(Installation)
admin.site.register(Depannage)
admin.site.register(Retrait)
admin.site.register(Routeur)
admin.site.register(Antenne)
