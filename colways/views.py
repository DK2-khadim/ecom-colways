from django.shortcuts import render
from produits.models import *


def accueil(request):
    man = Catalogue.objects.get(Cats="Homme")
    woman = Catalogue.objects.get(Cats="Femme")
    childreen = Catalogue.objects.get(Cats="Enfants")
    accessories = Catalogue.objects.get(Cats="Accessoires")
    electronic = Catalogue.objects.get(Cats="Electronique")
    home = Catalogue.objects.get(Cats="Maison")
    clothes = Catalogue.objects.get(Cats="Vetements")
    car = Catalogue.objects.get(Cats="Vehicules")
    accessoriesproducts = Produit.objects.filter(Categorie=accessories)
    electronicproducts = Produit.objects.filter(Categorie=electronic)
    homeproducts = Produit.objects.filter(Categorie=home)
    clothesproducts = Produit.objects.filter(Categorie=clothes)
    carproducts = Produit.objects.filter(Categorie=car)
    childreenproducts = Produit.objects.filter(Categorie=childreen)
    womanproducts = Produit.objects.filter(Categorie=woman)
    manproducts = Produit.objects.filter(Categorie=man)
    mostpopular = Produit.objects.all()
    context = {
        'manproducts':manproducts,
        'womanproducts':womanproducts,
        'childreenproducts':childreenproducts,
        'electronicproducts':electronicproducts,
        'accessoriesproducts':accessoriesproducts,
        'homeproducts':homeproducts,
        'chothesproducts':clothesproducts,
        'carproducts':carproducts,
        'mostpopular':mostpopular,
    }
    return render(request,"index.html",context)