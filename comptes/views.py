from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from comptes.models import *
from membres.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
# Partie Inscription

def signup(request):
    email_used = False
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User()
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        user.email = email
        user.set_password(password)
        if User.objects.filter(email=email).exists():
            email_used = True
        else:
            user.save()
            profil = Profil()
            profil.Profil_User = user
            profil.save()
            messages.success(request,"Inscription réussie !")
            return redirect("accueil")
    context = {
        'email_used' : email_used,
    }
    return render(request,"comptes/signup.html",context)

# Partie Connexion

def signin(request):
    error = False
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = ""
        try:
            username = User.objects.get(email=email.lower()).username
        except ObjectDoesNotExist:
            error = True
        finally:
            pass
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"Bienvenue sur colways")
            return redirect("homepage")
        else:
            error = True
    context={
        "error":error,
    }
    return render(request,"comptes/signin.html",context)


# Partie Deconnexion 

def logout_view(request):
    logout(request)
    return redirect("accueil")
