from django.shortcuts import render
from shoe.models import *

def index(request):
    items = Item.objects.filter(is_sold=False)
    
    return render(request, 'core/index.html', {
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')