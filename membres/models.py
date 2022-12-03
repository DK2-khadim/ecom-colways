from django.db import models
from django.contrib.auth.models import User


################################### Profil ######################################

class Profil(models.Model):
    regions = (
        ("Dakar","dakar"),
        ("Thiès","thiès"),
        ("Diourbel","diourbel"),
        ("Louga","louga"),
        ("Saint-Louis","st-louis"),
        ("Kaolack","kaolack"),
        ("Fatick","fatick"),
        ("Kaffrine","kaffrine"),
        ("Sédhiou","sédhiou"),
        ("Tambacounda","tambacounda"),
        ("Matam","matam"),
        ("Ziguinchor","ziguinchor"),
        ("Kolda","Kolda"),
        ("Kédougou","kédougou")
    )
    Profil_User = models.ForeignKey(User,on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to="users_profil/",blank=True)
    Telephone = models.IntegerField(null=True)
    Adresse1 = models.CharField(max_length=200)
    Adresse2 = models.CharField(max_length=200)
    Description = models.TextField()
    Region = models.CharField(max_length=11,choices=regions)
    Link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Profil_User.username


