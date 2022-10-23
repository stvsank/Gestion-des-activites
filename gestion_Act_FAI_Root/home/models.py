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
    job = models.CharField(max_length=40,choices=choix,default='Technicien')
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


# # activitées
# class Visite(models.Model):
#     date : models.DateField(auto_now=True)
#     possible = models.BooleanField(default=True)
#     comment : models.CharField(max_length=250)
    

# class Installation(models.Model):
#     date : models.DateField(auto_now=True)
#     comment : models.CharField(max_length=250)


# class Depannage(models.Model):
#     date : models.DateField(auto_now=True)
#     comment : models.CharField(max_length=250)
#     etat_lien : models.BooleanField(default=True)


# class Retrait(models.Model):
#     date : models.DateField(auto_now=True)
#     comment : models.CharField(max_length=250)


# class Caracteristique(models.Model):
#     imageCaracteristique = models.ManyToManyField(ImageCaractéristique, blank=True)
#     imageMateriel = models.ManyToManyField(ImageMateriel, blank=True)
        
# class Client(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     phone_number = models.IntegerField()


# class Device(models.Model):
#     num_serie = models.CharField(primary_key=True,max_length=30)
#     type_app = models.CharField(max_length=40)
#     nom = models.CharField(max_length=40)
#     new = models.BooleanField(default=True)


# class Localisation(models.Model):
#     # coordonnee = 
#     comment = models.CharField(max_length=250)





# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     category = models.CharField(max_length=50)
#     released_date = models.DateField(default = datetime.now())
#     author = models.ForeignKey(Person, on_delete=models.CASCADE)
#     # If you delete a person, his posts will be also deleted

#     def __str__(self):
#         return f'{self.title}'