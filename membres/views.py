from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from membres.models import *
from django.db.models import Q 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from produits.models import *

@login_required
def homepage(request):
    accueil = True
    profil = get_object_or_404(Profil,Profil_User=request.user)
    mesproduits = Produit.objects.filter(Auteur=request.user)
    paginator = Paginator(mesproduits,9)
    page = request.GET.get('page')
    try : 
        produits = paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    context = {
        'profil':profil,
        'produits':produits,
        'accueil':accueil
    }
    return render(request,"membres/homepage.html",context)

@login_required
def monprofil(request):
    user = request.user
    profil = get_object_or_404(Profil,Profil_User=user)
    if request.method == "POST":
        lastname = request.POST["lastname"]
        firstname = request.POST["firstname"]
        username = request.POST["username"]
        email = request.POST["email"]
        adresse1 = request.POST["adresse1"]
        adresse2 = request.POST["adresse2"]
        region = request.POST["region"]
        telephone = request.POST["telephone"]
        link = request.POST["link"]
        bio = request.POST["bio"]

        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        user.email = email
        user.save()

        try:
            profil.Photo = request.FILES["photo"]
        except:
            print("pas de photo")
        finally:
            pass
        profil.Adresse1 = adresse1
        profil.Adresse2 = adresse2
        profil.Description = bio
        profil.Telephone = telephone
        profil.Link = link
        profil.Region = region
        profil.save()
    context = {
        'user':user,
        'profil':profil,
    }
    return render(request,"membres/monprofil.html",context)


    # query = request.GET.get('q')
    # if query:
    #     post_list = Post.objects.filter(
    #         Q(titre_Post__icontains=query)|
    #         Q(auteur__username=query)|
    #         Q(contenu__icontains=query)
    #     )