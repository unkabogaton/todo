
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            items= Item.objects.all().order_by('-created')
            messages.success(request,('A New Task Has Been Successfully Added to Your Notes!'))
            return render(request,'index.html', context={'items': items, 'form':form})
    items= Item.objects.all().order_by('-created')
    return render(request,'index.html', context={'items': items})

def delete(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.delete()
    a=item.item + " Has Been Sucessfully Deleted"
    messages.success(request, (a))
    return redirect('index')

def cross_off(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=True
    item.save()
    a= 'Congrats! ' + item.item + " Has Been Completed!"
    messages.success(request,(a))
    return redirect('index')

def uncross(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=False
    item.save()
    a= item.item + " Has Been Set to Ongoing!"
    messages.success(request,(a))
    return redirect('index')

def edit(request, item_id):
    if request.method == 'POST':
        item=Item.objects.get(pk=item_id)
        form=ItemForm(request.POST, instance=item)
        if form.is_valid():
            item.save()
            a = item.item + ' Has Been Successfully Updated!'
            messages.success(request,(a))
            return redirect('index')
        else:
            return redirect('index')

def search(request):
    query=request.GET.get("q")
    if query:
        items=Item.objects.filter(Q(item__icontains=query)|Q(description__icontains=query)).distinct().order_by('-created')
        a= 'Matched Results for ' + query + ' Are Ready'
        messages.success(request,(a))
        return render(request,'index.html', context={'items': items})
    else:
        return redirect('index')

def completed_task(request):
    items=Item.objects.filter(completed=True)
    messages.success(request,('Showing All Completed Task'))
    return render(request,'index.html', context={'items': items})

def ongoing_task(request):
    items=Item.objects.filter(completed=False)
    messages.success(request,('Showing All Ongoing Task'))
    return render(request,'index.html', context={'items': items})

def all_completed(request):
    items=Item.objects.filter(completed=False)
    for item in items:
        item.completed=True
        item.save()
    messages.success(request,('All Tasks are set to Completed'))
    return redirect('index')

def all_ongoing(request):
    items=Item.objects.filter(completed=True)
    for item in items:
        item.completed=False
        item.save()
    messages.success(request,('All Tasks are set to Ongoing'))
    return redirect('index')

def del_completed(request):
    items=Item.objects.filter(completed=True)
    for item in items:
        item.delete()
    messages.success(request,('All Completed Tasks are Deleted'))
    return redirect('index')

def del_all(request):
    items=Item.objects.all()
    for item in items:
        item.delete()
    messages.success(request,('All Tasks are Deleted'))
    return redirect('index')
