
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import salir

urlpatterns = [
    path("login/", 
         LoginView.as_view(template_name="users/login.html"), 
         name="login"
         ),
    path("loguin/", 
         LoginView.as_view(), 
         name="loguin"
         ),
    path("logout/", salir , name="logout"),
]
