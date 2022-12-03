from django.contrib import admin
from membres.models import *

class ProfilAdmin(admin.ModelAdmin):
    list_display = ("Profil_User","Photo","Adresse1","Telephone")

admin.site.register(Profil,ProfilAdmin)
