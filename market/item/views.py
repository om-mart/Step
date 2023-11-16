from django.shortcuts import render, get_object_or_404
from .models import Item
from item.forms import ItemForm
from django.contrib import messages


# renders form to create a new listing
# handles form validation / saving
def createItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ItemForm()  # Create a new empty form after saving
            messages.success(request, 'Item listed successfully!')
    else:
        form = ItemForm()

    return render(request, 'item/create-item.html', {
        'form': form
    })

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
    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Women'
    })

def men(request):
    category_items = Item.objects.filter(category__name="Men", is_sold=False)
    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Men'
    })


def kids(request):
    category_items = Item.objects.filter(category__name="Kids", is_sold=False)
    return render(request, 'item/category-items.html', {
         'category_items': category_items,
         'category': 'Kids'
    })

