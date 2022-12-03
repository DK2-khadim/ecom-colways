from django.db import models
from django.contrib.auth.models import User

######################################### Catalogue (Nos domaines) #####################################

class Catalogue(models.Model):
    choix = (
        ("Femme","femme"),
        ("Homme","homme"),
        ("Enfants","enfants"),
        ("Accessoires","accessoires"),
        ("Electronique","electronique"),
        ("Véhicules","vehicules"),
        ("Vetements","vetements"),
        ("Maison","maison"),
        ("Autre","autre")
    )
    Cats = models.CharField(max_length=12,choices=choix)

    def __str__(self):
        return self.Cats

####################################### Produits ###############################################
   
class Produit(models.Model):
    tailles = (
        # vetements
        ("S","Taille S"),
        ("XS","Taille XS"),
        ("M","Taille M"),
        ("L","Taille L"),
        ("XL","Taille XL"),
        ("XXL","Taille XXL"),
        ("XXXL","Taille XXXL"),
        # chaussures
        ("12-14","12-14"),
        ("14-16","14-16"),
        ("16-18","16-18"),
        ("18-20","18-20"),
        ("20-22","20-22"),
        ("22-24","22-24"),
        ("24-26","24-26"),
        ("26-28","26-28"),
        ("28-30","28-30"),
        ("30-32","30-32"),
        ("32-34","32-34"),
        ("34-36","34-36"),
        ("36-38","36-38"),
        ("38-40","38-40"),
        ("40-42","40-42"),
        ("42-44","42-44"),
        ("44-46","44-46"),
        # poids 
        ("0-2Kg","0-2Kg"),
        ("2-4Kg","2-4Kg"),
        ("4-6Kg","4-6Kg"),
        ("6-8Kg","6-8Kg"),
        ("8-10Kg","8-10Kg"),
        ("+10Kg","+10Kg"),
        ("+20Kg","+20Kg"),
        # bagues 
        ("14.1-14.9mm","14.1-14.9mm"),
        ("15.1-15.9mm","15.1-15.9mm"),
        ("16.1-16.9mm","16.1-16.9mm"),
        ("17.1-17.9mm","17.1-17.9mm"),
        ("Ajustable","ajustable"),
        # parfum ou autre
        ("Petit","petit modèle"),
        ("Grand","grand modèle"),
        # Maison 
        ("Petit Terrain","petit terrain"),
        ("Grand Terrain","grand terrain"),
        ("Appartement","appartement"),
        ("Chambres + salon","chambres + salon"),
        ("Chambres + salon + cuisine","Chambres + salon + cuisine"),
        # Aucune 
        ("Autre","autre")
    )
    couleurs = (
        ("Rouge","rouge"),
        ("Vert","verte"),
        ("Bleu","bleu"),
        ("Noir","noir"),
        ("Jaune","jaune"),
        ("Marron","marron"),
        ("Rose","rose"),
        ("Blanc","blanche"),
        ("Gris","gris"),
        ("Orange","orange"),
        ("Violet","violette"),
        ("Multicouleur","multicouleur")
    )
    etats = (
        ("Deuxieme main","deuxieme main"),
        ("Bon état","ken utilisé ko lou bari"),
        ("Neuf","ken utilisé kou"),
        ("Neuf avec étiquette","bou bess takk")
    )
    marques = (
        # chaussures ou vetements 
        ("Nike","nike"),
        ("Adidas","adidas"),
        ("NB","new balance"),
        ("Lacoste","lacoste"),
        ("Calvin Klein","calvin klein"),
        ("Polo","polo"),
        ("Fila","fila"),
        ("Chanel","chanel"),
        ("Puma","puma"),
        ("Vans","vans"),
        ("Gucci","gucci"),
        ("Balenciaga","balenciaga"),
        ("Converse","converse"),
        ("Vogue","vogue"),
        ("Levi's","levi's"),
        ("Tommy Hilfiger","tommy hilfiger"),
        ("Louis Vuitton","louis vuitton"),
        ("Ascis","ascis"),
        ("D&G","dolce gabbana"),
        # Voitures 
        ("Audi","audi"),
        ("Jeep","jeep"),
        ("Kia","kia"),
        ("Hyundai","hyundai"),
        ("Bentley","bentley"),
        ("Citroen","citroen"),
        ("Renault","renault"),
        ("Volkswagen","volkswagen"),
        ("OPEL","opel"),
        ("Peugeot","peugeot"),
        ("Bugatti","bugatti"),
        ("Nissan","Nissan"),
        ("Toyota","toyata"),
        ("Suzuki","suzuki"),
        ("Mercedes-Bnez","mercedes-benz"),
        ("Volvo","volvo"),
        ("Ford","ford"),
        ("Smart","smart"),
        # Accessoires
        ("Apple","apple"),
        ("Sony","sony"),
        ("Huawei","huawei"),
        ("Asus","asus"),
        ("Alcatel","alcatel"),
        ("Nokia","nokia"),
        ("ZTE","zte"),
        ("Motorola","motorola"),
        ("Wiko","wiko"),
        ("LG","lg"),
        ("htc","htc"),
        ("Dell","dell"),
        ("Samsung","samsung"),
        ("Tecno","tecno"),
        ("Itel","itel"),
        ("Hp","hp"),
        ("BlackBerry","blackberry"),
        ("Xiaomi","xiaomi"),
        ("Philips","philips"),
        ("Sharp","sharp"),
        ("Siesmens","siesmens"),
        ("Vodafone","vodafone"),
        ("Sagem","sagem"),
        ("Universel","universel"),
        # Autre
        ("Autre","autre")
    )
    Auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    Categorie = models.ForeignKey(Catalogue,on_delete=models.CASCADE)
    Nom = models.CharField(max_length=250,null=True)
    Ref = models.CharField(max_length=250,null=True)
    Taille = models.CharField(max_length=26,choices=tailles)
    Marque = models.CharField(max_length=20,choices=marques)
    Etat = models.CharField(max_length=20,choices=etats)
    Couleur = models.CharField(max_length=20,choices=couleurs)
    Echange = models.BooleanField(default=False)
    Prix = models.IntegerField()
    Description = models.CharField(max_length=25)
    Photo1 = models.ImageField(upload_to="products/",blank=False,null=False)
    Photo2 = models.ImageField(upload_to="products/",blank=True,null=True)
    Photo3 = models.ImageField(upload_to="products/",blank=True,null=True)
    Likes = models.ManyToManyField(User,blank=True,related_name="likes")
    

    def all_likes(self):
        return self.Likes.count()

    def __str__(self):
        return self.Auteur.username
    
    