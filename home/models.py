from django.db import models
from datetime import datetime, date

class Employe(models.Model):
    choix = [
        ('DG', 'Directeur Générale'),
        ('DAF', 'Directeur Affaire Financière'),
        ('DT', 'Directeur Technique'),
        ('Ingénieur', 'Ingénieur'),
        ('Technicien', 'Technicien'),
        ('Commercial', 'Commercial'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    job = models.CharField(max_length=20,choices=choix,default='Technicien')
    phone_number = models.IntegerField()
    leave = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'    


class Conge(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.debut} - {self.fin}'    

# class Image(models.Model):
#     image = models.URLField()

# class ImageProfile(Image):
#     employe = models.ForeignKey(Employe, on_delete=models.CASCADE)

# class ImageCaractéristique(Image):
#     pass

# class ImageMateriel(Image):
#     pass

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# activitées
choix = [
    ('oui','Oui'),
    ('non','Non'),
]
class Visite(models.Model):
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    possible = models.CharField(max_length=4,choices=choix,default="oui")
    comment = models.TextField(max_length=250)
    employe = models.ManyToManyField(Employe, blank=True)
    client = models.OneToOneField(Client,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.heure} {self.client} {self.employe}'
    

class Installation(models.Model):
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)
    etat = models.CharField(max_length=4,choices=choix, default="oui")
    employe = models.ManyToManyField(Employe, blank=True)
    client = models.OneToOneField(Client,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.heure} {self.client}'

        
class Depannage(models.Model):
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)
    etat = models.CharField(max_length=4,choices=choix, default="oui")
    employe = models.ManyToManyField(Employe, blank=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.heure} {self.client}'

 
class Retrait(models.Model):
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)
    reste = models.CharField(max_length=4,choices=choix, default="non")
    employe = models.ManyToManyField(Employe, blank=True)
    client = models.OneToOneField(Client,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.heure} {self.client}'

 

# class Caracteristique(models.Model):
#     imageCaracteristique = models.ManyToManyField(ImageCaractéristique, blank=True)
#     imageMateriel = models.ManyToManyField(ImageMateriel, blank=True)
        


class Routeur(models.Model):
    num_serie = models.CharField(primary_key=True,max_length=30)
    nom = models.CharField(max_length=40)
    new = models.BooleanField(default=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)


class Antenne(models.Model):
    num_serie = models.CharField(primary_key=True,max_length=30)
    nom = models.CharField(max_length=40)
    new = models.BooleanField(default=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)



# class Localisation(models.Model):
#     # coordonnee = 
#     comment = models.CharField(max_length=250)

