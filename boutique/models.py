from django.db import models
from django.contrib.auth.models import User
from produits.models import *

##################################### Boutique ####################################

class Boutique(models.Model):
    Gerant = models.ForeignKey(User,on_delete=models.CASCADE)
    Logo = models.ImageField(upload_to="boutiques/",null=False)
    Nom = models.CharField(max_length=100)
    Description = models.CharField(max_length=250)
    Telephone = models.IntegerField()
    Adresse = models.CharField(max_length=300)
    Produits = models.ForeignKey(Produit,on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.Gerant,self.Nom)

  
    

