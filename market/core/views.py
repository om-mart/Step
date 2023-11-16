from django.shortcuts import render
from item.models import Item 

# render homepage
def home(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    
    return render(request, 'core/home.html', {
        'items': items
    })

# render contact page
def about(request):
    return render(request, 'core/about.html')

# render owner page
def owner(request):
    return render(request, 'core/owner.html')