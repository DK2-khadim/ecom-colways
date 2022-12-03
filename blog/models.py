from django.db import models
from django.contrib.auth.models import User

######################################### Post ######################################

class Post(models.Model):
    Photo = models.ImageField(upload_to="posts")
    Titre = models.CharField(max_length=200)
    Contenu = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Loves = models.ManyToManyField(User,related_name="loves",blank=True)

    class Meta:
        ordering = ['-id']

    def all_loves(self):
        return self.Loves.count()

    def __str__(self):
        return self.Titre

class Comment(models.Model):
    Comment_Post = models.ForeignKey(Post,on_delete=models.CASCADE)
    Comment_User = models.ForeignKey(User,on_delete=models.CASCADE)
    Comment_Content = models.TextField()
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.Comment_Post.Titre,str(self.Comment_User))
    

######################################### Forum #######################################

