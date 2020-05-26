#redirected here from mywebsite.url, the controller looks here
from django.urls import path
from . import views

app_name  = "main"
urlpatterns = [
    
    #the controller is then directed to views, for a response or render a webpage for every url
    path('',views.homepage,name = "homepage"),
    path('register/',views.register,name = "register"),
    path('logout/',views.logout_request, name = "logout"),
    path('login/',views.login_request, name = "login"),
    path('<single_slash>',views.single_slash, name = "single_slash"),

]
