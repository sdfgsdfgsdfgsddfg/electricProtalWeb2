from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path('',views.home,name='home'),
    path('consultants',views.consultants,name='consultants'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
]