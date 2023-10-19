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

    return render(request, 'core/create-item.html', {
        'form': form
    })

# lists details of an item
def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item/detail.html', {
        'item': item
    })
