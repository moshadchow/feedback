from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('portfolio_details/<int:id>/', views.portfolio_details,name='portfolio_dtl'),
    path('inner_page/', views.inner_page,name='inner_pg'),
]