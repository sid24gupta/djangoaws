from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# from second_application.models import Product
from .models import Product

def help(request):

    # data = { 'value1' : 'Help page from second_application'}
    x = Product.objects.all()
    data = {'value1':x}
    return render(request,'second_application/help.html',context=data)
