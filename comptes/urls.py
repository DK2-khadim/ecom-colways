from django.contrib import admin
from django.urls import path,include
from comptes import views

urlpatterns = [
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("logout",views.logout_view,name="logout"),
]
