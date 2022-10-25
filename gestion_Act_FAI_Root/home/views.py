from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Employe, Conge, Visite
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
    installation = [
    {
        'heures' : '8h 50mn',
        'client' : 
            {
                'last_name':'Mark', 
                'first_name' : 'Tanga'
            },
        'etat' : 'oui',
        'employes': [
            {
                'last_name':'Sankara', 
                'first_name' : 'Steve'
            }
        ],
        'comment' : 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longerThis is a wider card with supporting text below as a natural lead-in to additional content.This is a wider card with supporting text below as'
    },
    {
        'heures' : '8h 40mn',
        'client' :
            {
                'last_name':'Kaled', 
                'first_name' : 'Brou'
            },  
        'etat' : 'oui',
        'employes': [
            {
                'last_name':'Sankara', 
                'first_name' : 'Steve'
            },
            {
                'last_name':'Yan', 
                'first_name' : 'Koffi'
            }
        ],
        'comment' : 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longerThis is a wider card with supporting text below as a natural lead-in to additional content.This is a wider card with supporting text below as'
    },
    ]
    depannage = [
    {
        'heures' : '8h 40mn',
        'client' : 
            {
                'last_name':'Mark', 
                'first_name' : 'Tanga'
            },
        'etat' : 'oui',
        'employes': [
            {
                'last_name':'Sankara', 
                'first_name' : 'Steve'
            }
        ],
        'comment' : 'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longerThis is a wider card with supporting text below as a natural lead-in to additional content.This is a wider card with supporting text below as'
    }
    ]
    retrait = []

    context = {
        'nombre' : 2,
        'visites' : visite,
        'nbr_visite' : len(visite),
        'installations' : installation,
        'nbr_installation' : len(installation),
        'depannages' : depannage, 
        'nbr_depannage' : len(depannage),
        'retraits' : retrait,
        'nbr_retrait' : len(retrait),
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

def clients(request,id = 0):
    return render(request,'home/clients.html')

def technique(request):
    return render(request,'home/technique.html')

def statistique(request):
    return render(request,'home/statistique.html')


   
