from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('Articles',views.articles,name="articles"),
    path('detail_post',views.detail_post,name="detail_post"),
    path('Contactez_Nous',views.contactezNous,name="contactezNous"),
]
