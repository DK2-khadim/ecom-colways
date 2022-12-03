from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ("Titre","Photo","created")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("Comment_Post","Comment_User","added")

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

