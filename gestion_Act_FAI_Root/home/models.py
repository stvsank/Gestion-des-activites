from django.db import models
# from datetime import datetime, date

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    conge = models.BooleanField(default=True)
    visite = models.IntegerField()
    installation = models.IntegerField()
    depannage = models.IntegerField()
    retrait = models.IntegerField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     category = models.CharField(max_length=50)
#     released_date = models.DateField(default = datetime.now())
#     author = models.ForeignKey(Person, on_delete=models.CASCADE)
#     # If you delete a person, his posts will be also deleted

#     def __str__(self):
#         return f'{self.title}'
    
# class ImageProfile (models.Model):
#     person = models.OneToOneField(
#         Person,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     image = models.URLField()

#     def __str__(self):
#         return f'ImageProfile of {self.person}'