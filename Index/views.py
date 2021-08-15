from django.shortcuts import render
from .models import about
from .models import slider
from .models import feature
from .models import service
from .models import team
from .models import client
from .models import category
from .models import product
from django.db import connection
# Create your views here.


def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    featuredata = feature.objects.all()
    servicedata = service.objects.all()
    teammember = team.objects.all()
    clientdata = client.objects.all()
    categorydata = category.objects.all()
    productdata = product.objects.all()
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.id,c.cat_nm cat_nm,p.p_name,p.image FROM index_product p JOIN index_category c ON p.cat_id=c.id")
        portfolio = cursor.fetchall()
        print(portfolio)
    #print(category)
    context = {
        "about": aboutdata,
        "slider": sliderdata,
        "features": featuredata,
        "services": servicedata,
        "teams" : teammember,
        "clients": clientdata,
        "categories": categorydata,
        "products" : productdata,
        "portfolios" : portfolio
    }
    return render(request, "index.html", context)


def aboutus(request):
    return render(request, "about.html")
    
def portfolio_details(request,id):
    pi = product.objects.get(pk=id);
    context = {'product':pi}
    return render(request, "portfolio_details.html",context)

def inner_page(request):
    return render(request, "inner_page.html")