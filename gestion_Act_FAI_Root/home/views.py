from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Employe, Conge
from datetime import datetime, date

# takes a request, returns a response
def index(request):
    users = Employe.objects.all()

###  Détermine si oui ou non un employé est en congé ###
    for user in users:
        conge = Conge.objects.filter(employe = user)
        if conge: 
            a = len(conge)-1
            conge = conge[a]
            debut = datetime.strptime(str(conge.debut), '%Y-%m-%d')
            fin = datetime.strptime(str(conge.fin), '%Y-%m-%d')
            if debut < datetime.now() and fin > datetime.now():
                user.leave = True
            else:
                user.leave = False
###
    context = {
        'users' : users,
        'login' : False
    }

    return render(request, 'home/index.html', context)


def userSpace(request):
    return HttpResponse("Espace utilisateur")

def historique(request):
    context = {
        'login' : True
    }
    return render(request, 'home/historique.html', context)

def infoActEmploy(request,id):
    users = Employe.objects.all()
    for user in users:
        if user.pk == id:
            context = {
                'user' : user,
                'login' : False
            }
    return render(request, 'home/infoActEmploy.html',context)

   
