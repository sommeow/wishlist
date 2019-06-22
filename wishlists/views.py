from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

# Define the home view
class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', { 'items': items })

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', { 'items': items })

def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'items/detail.html', { 'item': item })