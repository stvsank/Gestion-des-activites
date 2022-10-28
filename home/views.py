from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Employe, Conge, Visite, Installation, Depannage, Retrait, Client, Routeur, Antenne
from datetime import datetime, date
from django.db.models import Q #filter() or logique 

# takes a request, returns a response
def index(request):
    users = Employe.objects.all()

###  Détermine si oui ou non un employé est en congé
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
    visite = Visite.objects.filter(date=datetime.now())
    installation = Installation.objects.filter(date=datetime.now())
    depannage = Depannage.objects.filter(date=datetime.now())
    retrait = Retrait.objects.filter(date=datetime.now())

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
    visite = Visite.objects.filter(employe__pk=id,date=datetime.now())
    installation = Installation.objects.filter(employe__pk=id,date=datetime.now())
    depannage = Depannage.objects.filter(employe__pk=id,date=datetime.now())
    retrait = Retrait.objects.filter(employe__pk=id,date=datetime.now())
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
        routeur = Routeur.objects.filter(client = user)
        antenne = Antenne.objects.filter(client = user)
        client = {
            'visites' : visite,
            'installations' : installation,
            'depannages' : depannage, 
            'retraits' : retrait,
            'user' : user,
            'routeurs' : routeur,
            'antennes' : antenne,

        }
        clients.append(client)
        context = {
            'clients' : clients
        }
    return render(request,'home/clients.html',context)

def technique(request):
    users = Employe.objects.filter(Q(job='Technicien') | Q(job='Ingénieur'))
    employes = []
    for user in users:
        visite = Visite.objects.filter(employe = user)
        installation = Installation.objects.filter(employe = user)
        depannage = Depannage.objects.filter(employe = user)
        retrait = Retrait.objects.filter(employe = user)
    # nombre de jour de congé
        conges = Conge.objects.filter(employe = user)
        jours = 0  
        i = 1 
        for conge in conges:
            debut = datetime.strptime(str(conge.debut), '%Y-%m-%d')
            fin = datetime.strptime(str(conge.fin), '%Y-%m-%d')
            if fin > debut:
                tmp = str(fin - debut)
                tmp = int(tmp[0:len(tmp)-14])
                jours += tmp
                i += 1
    ##

    # trouve le nombre d'installation qui a été dépanné
        panne = 0
        for x in installation:
            if Depannage.objects.select_related("client").all().filter(client = x.client):
                panne += 1
        ###
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
            'panne' : panne,
            'jours' : jours,
            'total' : len(visite) + len(installation) + len(depannage) + len(retrait), # nombre total d'activité
        }
        employes.append(employe)
# classement en fonction du nombre total d'activité
    employes = sorted(employes, key=lambda t: t['total'], reverse=True)
    pk = 1
    for employe in employes:
        employe.update({'pk' : pk})
        pk += 1
###
    context = {
        'employes' : employes
    }
    return render(request,'home/technique.html',context)

def statistique(request):
    return render(request,'home/statistique.html')

# Entry.objects.get(headline__contains='Lennon')
# Entry.objects.filter(pub_date__lte='2006-01-01