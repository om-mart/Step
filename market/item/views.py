from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item
from item.forms import ItemForm
from django.contrib import messages

# renders and saves form to create a new listing
def createItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid(): 
            new_item = form.save()
            messages.success(request, 'Item listed successfully!')
            return redirect('item:detail', id=new_item.id)
    else:
        form = ItemForm()

    return render(request, 'item/create-item.html', {
        'form': form
    })

# update an existing listing
def editItem(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        msg = messages.success(request, "Listing Updated Successfully")
        form.save()
        return redirect('item:detail', id=id)
    
    return render(request, 'item/edit-item.html', {
        'form': form,
        'item': item,
    })

def deleteItem(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    messages.success(request, 'Item successfully deleted!')

    return redirect('core:home')

# lists details of an item
def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=id)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

def women(request):
    category_items = Item.objects.filter(category__name="Women", is_sold=False)
    
    query = request.GET.get('query', '')
    if query:
        category_items = category_items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Women',
         'query': query,
    })

def men(request):
    category_items = Item.objects.filter(category__name="Men", is_sold=False)
    
    query = request.GET.get('query', '')
    if query:
        category_items = category_items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Men',
         'query': query,
    })


def kids(request):
    category_items = Item.objects.filter(category__name="Kids", is_sold=False)
    
    query = request.GET.get('query', '')
    if query:
        category_items = category_items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Kids',
         'query': query,
    })

