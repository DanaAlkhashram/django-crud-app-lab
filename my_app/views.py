from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/item_detail.html', {'item': item})

class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'description', 'price']
    template_name = 'items/item_form.html'
    success_url = '/items/'  

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'description', 'price']
    template_name = 'items/item_form.html'
    success_url = '/items/'  
    
class ItemDelete(DeleteView):
    model = Item
    template_name = 'items/item_confirm_delete.html'
    success_url = '/items/'   
