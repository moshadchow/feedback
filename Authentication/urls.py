from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginPage,name='login'),
    path('registrationPage/', views.registrationPage,name='registration'),
    path('forgot-password/', views.forgotpassword,name='forgotpassword'),
    path('logout/', views.userlogout,name='logout'),
]