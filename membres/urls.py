from django.contrib import admin
from django.urls import path,include
from membres import views
urlpatterns = [
    path("home",views.homepage,name="homepage"),
    path("membre/mon_profil",views.monprofil,name="monprofil"),
]
