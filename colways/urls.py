"""colways URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from colways import views
#from django.conf.urls import url
# Configuration des medias 
from django.conf import settings 
from django.conf.urls.static import static  
# Importer les views du django
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.accueil,name="accueil"),
    # les urls de l'app comptes
    path('comptes/',include('comptes.urls')),
    # les urls de l'app blog
    path('blog/',include('blog.urls')),
    # les urls de l'app produits
    path('produits/',include('produits.urls')),
    # les urls de l'app membre 
    path('',include('membres.urls')),

    # for django social 
    #path('',include('django.contrib.auth.urls')),
    #path('oauth/',include('social_django.urls',namespace="social")),
    # Password Reset url 
    path('password_reset',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
]

# A ne pas supprimer | c'est pour l'affichage des photos 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
