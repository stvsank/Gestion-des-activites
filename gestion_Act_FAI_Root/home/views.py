from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def index(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    }

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects,
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


   
