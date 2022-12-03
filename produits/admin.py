from django.contrib import admin
from produits.models import *


class CatalogueAdmin(admin.ModelAdmin):
    list_display = ("Cats",)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ("Auteur","Categorie","Taille","Marque","Echange","Photo1")

admin.site.register(Catalogue,CatalogueAdmin)
admin.site.register(Produit,ProduitAdmin)
