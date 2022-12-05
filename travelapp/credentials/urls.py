from django.urls import path
from . import views

app_name = "credentials"

urlpatterns = [
    path('register/', views.signup, name="registeruser"),
    path('login/', views.signin, name="loginuser"),
    path('logout/', views.signout, name="logoutuser"),
]
