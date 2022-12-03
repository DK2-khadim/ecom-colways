from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from membres.models import *
from django.db.models import Q 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from produits.models import *


def shopping(request):
    # To do
    return render(request,"produits/shopping.html")

def detail_produit(request,id):
    profil = Profil.objects.get(Profil_User=request.user)
    produit = get_object_or_404(Produit, id=id)
    profil_vendeur = Profil.objects.get(Profil_User = produit.Auteur )
    context = {
        'profil':profil,
        'produit':produit,
        'profil_vendeur':profil_vendeur,
    }
    return render(request,"produits/detail_produit.html",context)

@login_required
def add_product(request):
    profil = get_object_or_404(Profil,Profil_User=request.user)
    if request.method == "POST":
        couleur = request.POST["couleur"]
        etat = request.POST["etat"]
        echange = request.POST["echange"]
        description = request.POST["description"]
        nom = request.POST["nom"]
        prix = request.POST["prix"]
        photos = request.FILES.getlist('files')
        taille = request.POST['taille']
        marque = request.POST['marque']
        cats = request.POST['categorie']

        produit = Produit()
        categorie = Catalogue.objects.get(Cats=cats)
        produit.Photo1 = photos[0]
        produit.Photo2 = photos[1]
        produit.Photo3 = photos[2]
        
        produit.Auteur = request.user
        produit.Echange = echange
        produit.Taille = taille
        produit.Marque = marque
        produit.Nom = nom
        produit.Etat = etat
        produit.Prix = prix
        produit.Description = description
        produit.Couleur = couleur
        produit.Categorie = categorie

        produit.save()
        redirect('homepage')

    context={
        "profil":profil,
    }
    return render(request,"produits/add_produit.html",context)


@login_required
def update_product(request,id):
    produit = get_object_or_404(Produit,id=id)
    if request.method == "POST":
        nom = request.POST["nom"]
        prix = request.POST["prix"]
        description = request.POST["description"]

        produit.Nom = nom
        produit.Prix = prix
        produit.Description = description 

        produit.save()
        redirect('homepage')
    
    return render(request,"membres/homepage.html")


def dealofThe(request):
    # To do 
    return render(request,"produits/dealofthe.html")
