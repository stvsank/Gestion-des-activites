from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def index(request):
    users =[
    {
        'id' : 1,
        'first_name' : "John",
        'last_name' : "Doe",
        'job' : 'DG',
        'phone_number' : 70501111,
        'leave' : False
    },
    {
        'id' : 2,
        'first_name' : "Kévin",
        'last_name' : "Ouédraogo",
        'job' : 'DAF',
        'phone_number' : 70501112,
        'leave' : False
    },
    {
        'id' : 3,
        'first_name' : "Steven",
        'last_name' : "Da",
        'job' : 'DT',
        'phone_number' : 70501113,
        'leave' : False
    },
    {
        'id' : 4,
        'first_name' : "Hamed",
        'last_name' : "Barry",
        'job' : 'Technicien',
        'phone_number' : 70601000,
        'leave' : False
    },
    {
        'id' : 5,
        'first_name' : "Ali",
        'last_name' : "Ban",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : True
    },
    {
        'id' : 6,
        'first_name' : "Koffi",
        'last_name' : "Yan",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 7,
        'first_name' : "Omar",
        'last_name' : "Rafti",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 8,
        'first_name' : "Hamed",
        'last_name' : "Barry",
        'job' : 'Technicien',
        'phone_number' : 70601000,
        'leave' : False
    },
    {
        'id' : 9,
        'first_name' : "Ali",
        'last_name' : "Ban",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 10,
        'first_name' : "Koffi",
        'last_name' : "Yan",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 11,
        'first_name' : "Omar",
        'last_name' : "Rafti",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : True
    },

    ]


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
    users =[
    {
        'id' : 1,
        'first_name' : "John",
        'last_name' : "Doe",
        'job' : 'DG',
        'phone_number' : 70501111,
        'leave' : False
    },
    {
        'id' : 2,
        'first_name' : "Kévin",
        'last_name' : "Ouédraogo",
        'job' : 'DAF',
        'phone_number' : 70501112,
        'leave' : False
    },
    {
        'id' : 3,
        'first_name' : "Steven",
        'last_name' : "Da",
        'job' : 'DT',
        'phone_number' : 70501113,
        'leave' : False
    },
    {
        'id' : 4,
        'first_name' : "Hamed",
        'last_name' : "Barry",
        'job' : 'Technicien',
        'phone_number' : 70601000,
        'leave' : False
    },
    {
        'id' : 5,
        'first_name' : "Ali",
        'last_name' : "Ban",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : True
    },
    {
        'id' : 6,
        'first_name' : "Koffi",
        'last_name' : "Yan",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 7,
        'first_name' : "Omar",
        'last_name' : "Rafti",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 8,
        'first_name' : "Hamed",
        'last_name' : "Barry",
        'job' : 'Technicien',
        'phone_number' : 70601000,
        'leave' : False
    },
    {
        'id' : 9,
        'first_name' : "Ali",
        'last_name' : "Ban",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 10,
        'first_name' : "Koffi",
        'last_name' : "Yan",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : False
    },
    {
        'id' : 11,
        'first_name' : "Omar",
        'last_name' : "Rafti",
        'job' : 'Technicien',
        'phone_number' : 70601001,
        'leave' : True
    },
    ]
    for user in users:
        if user['id'] == id:
            context = {
                'user' : user,
                'login' : False
            }
    return render(request, 'home/infoActEmploy.html',context)

   
