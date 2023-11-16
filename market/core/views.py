from django.shortcuts import render
from item.models import Item 

# render homepage
def home(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    
    return render(request, 'core/home.html', {
        'items': items
    })

# render contact page
def contact(request):
    return render(request, 'core/contact.html')