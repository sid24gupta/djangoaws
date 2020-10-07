from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from second_application.models import Product

def index(request):
    x = Product.objects.all()

    return HttpResponse(x)