from django.contrib import admin
from django.urls import path,include
from produits import views

urlpatterns = [
    path('shopping',views.shopping,name="shopping"),
    path('detail_produit/<int:id>',views.detail_produit,name="detail_produit"),
    path('add_produit',views.add_product,name="add_product"),
    path('deal_of_the_day',views.dealofThe,name="dealofThe"),
]
