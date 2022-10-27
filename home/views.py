from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Employe, Conge, Visite, Installation, Depannage, Retrait, Client
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
### Fin
    context = {
        'users' : users,
        'login' : False
    }

    return render(request, 'home/index.html', context)


def userSpace(request):
    return HttpResponse("Espace utilisateur")

def historique(request):
    visite = Visite.objects.all()
    installation = Installation.objects.all()
    depannage = Depannage.objects.all()
    retrait = Retrait.objects.all()

    context = {
        'visites' : visite,
        'nbr_visite' : len(visite),
        'installations' : installation,
        'nbr_installation' : len(installation),
        'depannages' : depannage, 
        'nbr_depannage' : len(depannage),
        'retraits' : retrait,
        'nbr_retrait' : len(retrait),
    }
    return render(request, 'home/historique.html', context)

def infoActEmploy(request,id):
    visite = Visite.objects.filter(employe__pk=id)
    installation = Installation.objects.filter(employe__pk=id)
    depannage = Depannage.objects.filter(employe__pk=id)
    retrait = Retrait.objects.filter(employe__pk=id)
    user = Employe.objects.filter(pk=id)
    context = {
        'visites' : visite,
        'nbr_visite' : len(visite),
        'installations' : installation,
        'nbr_installation' : len(installation),
        'depannages' : depannage, 
        'nbr_depannage' : len(depannage),
        'retraits' : retrait,
        'nbr_retrait' : len(retrait),
        'user' : user[0]
    }
    return render(request, 'home/infoActEmploy.html',context)

def clients(request):
    users = Client.objects.all()
    clients = []
    for user in users:

        visite = Visite.objects.filter(client = user)
        installation = Installation.objects.filter(client = user)
        depannage = Depannage.objects.filter(client = user)
        retrait = Retrait.objects.filter(client = user)
        client = {
            'visites' : visite,
            'installations' : installation,
            'depannages' : depannage, 
            'retraits' : retrait,
            'user' : user,
        }
        clients.append(client)
        context = {
            'clients' : clients
        }
    return render(request,'home/clients.html',context)

def technique(request):
    users = Employe.objects.all()
    employes = []
    for user in users:

        visite = Visite.objects.filter(employe = user)
        installation = Installation.objects.filter(employe = user)
        depannage = Depannage.objects.filter(employe = user)
        retrait = Retrait.objects.filter(employe = user)
        employe = {
            'visites' : visite,
            'nbr_visite' : len(visite),
            'installations' : installation,
            'nbr_installation' : len(installation),
            'depannages' : depannage, 
            'nbr_depannage' : len(depannage),
            'retraits' : retrait,
            'nbr_retrait' : len(retrait),
            'user' : user,
        }
        employes.append(employe)
        context = {
            'employes' : employes
        }
    return render(request,'home/technique.html',context)

def statistique(request):
    return render(request,'home/statistique.html')