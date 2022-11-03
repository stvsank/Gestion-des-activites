from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Employe, Conge, Visite, Installation, Depannage, Retrait, Client, Routeur, Antenne
from datetime import datetime, date
from django.db.models import Q #filter() or logique 
from .forms import Dateform, Personform, Personform2

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
    }

    return render(request, 'home/index.html', context)


def userSpace(request):
    return HttpResponse("Espace utilisateur")

def historique(request,temps=datetime.now()):
### traitement pour la barre de recherche
    context={'form':Dateform()}
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = Dateform(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            form_date = str(request.POST['date'])
            temps = datetime.strptime(str(form_date), '%d/%m/%Y')
            tmp = temps      
    else:
        # GET, generate blank form
        context['form'] = Dateform()
###
    visite = Visite.objects.filter(date=temps)
    installation = Installation.objects.filter(date=temps)
    depannage = Depannage.objects.filter(date=temps)
    retrait = Retrait.objects.filter(date=temps)
    context.update({
        'visites' : visite,
        'nbr_visite' : len(visite),
        'installations' : installation,
        'nbr_installation' : len(installation),
        'depannages' : depannage, 
        'nbr_depannage' : len(depannage),
        'retraits' : retrait,
        'nbr_retrait' : len(retrait),
    })
    return render(request, 'home/historique.html', context)

def historiqueAll(request):
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
    return render(request, 'home/historiqueAll.html', context)

def infoActEmploy(request,id=0):
    context={'form':Personform()}
    temps=datetime.now()
### traitement pour la barre de recherche
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = Personform(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            nom=str(request.POST['last_name'])
            prenom=str(request.POST['first_name'])
            employe = False
            if nom != 'nom':
                employe = Employe.objects.filter(last_name__icontains=nom)
            if prenom != 'prénom':
                employe = Employe.objects.filter(first_name__icontains=prenom)
            if employe:
                id=employe[0].id
            form_date = str(request.POST['date'])
            if form_date != '31/12/2000':
                temps = datetime.strptime(str(form_date), '%d/%m/%Y')      
    else:
        # GET, generate blank form
        context['form'] = Personform()

    visite = Visite.objects.filter(employe__pk=id,date=temps)
    installation = Installation.objects.filter(employe__pk=id,date=temps)
    depannage = Depannage.objects.filter(employe__pk=id,date=temps)
    retrait = Retrait.objects.filter(employe__pk=id,date=temps)
    user = Employe.objects.filter(pk=id)
    context.update({
        'visites' : visite,
        'nbr_visite' : len(visite),
        'installations' : installation,
        'nbr_installation' : len(installation),
        'depannages' : depannage, 
        'nbr_depannage' : len(depannage),
        'retraits' : retrait,
        'nbr_retrait' : len(retrait),
    })
    if user:
        context.update({'user' : user[0]})
    return render(request, 'home/infoActEmploy.html',context)

def clients(request):
    client = []
    context={'form':Personform2()}
### traitement pour la barre de recherche
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = Personform2(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            nom=str(request.POST['last_name'])
            prenom=str(request.POST['first_name'])
            client = False
            if nom != 'nom':
                client = Client.objects.filter(last_name__icontains=nom)
            if prenom != 'prénom':
                client = Client.objects.filter(first_name__icontains=prenom)
            if client:
                id=client[0].id     
    else:
        # GET, generate blank form
        context['form'] = Personform2()
    clients = []
    for user in client:
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
        context.update({
            'clients' : clients,
        })
    return render(request,'home/clients.html',context)

def clientsAll(request):
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
    return render(request,'home/clientsAll.html',context)

def technique(request):
    employe = []
    context={'form':Personform2()}
### traitement pour la barre de recherche
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = Personform2(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            nom=str(request.POST['last_name'])
            prenom=str(request.POST['first_name'])
            employe = False
            if nom != 'nom':
                employe = Employe.objects.filter(last_name__icontains=nom)
            if prenom != 'prénom':
                employe = Employe.objects.filter(first_name__icontains=prenom)
            if employe:
                id=employe[0].id     
    else:
        # GET, generate blank form
        context['form'] = Personform2()
    employes = []
    for user in employe:
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
    context.update({
        'employes' : employes
    })
    return render(request,'home/technique.html',context)

def techniqueAll(request):
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
    return render(request,'home/techniqueAll.html',context)

def statistique(request):
    return render(request,'home/statistique.html')

# Entry.objects.get(headline__contains='Lennon')
# Entry.objects.filter(pub_date__lte='2006-01-01