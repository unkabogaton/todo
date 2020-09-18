
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as dj_login
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form=CreateUserForm() 
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('Account has been successfully created'))
            return redirect('login')
    return render (request, 'register.html', context={'form':form})
    

def login(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password did not match')
    return render (request, 'login.html', context={})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.delete()
    a=item.item + " Has Been Sucessfully Deleted"
    messages.success(request, (a))
    return redirect('index')

@login_required(login_url='login')
def cross_off(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=True
    item.save()
    a= 'Congrats! ' + item.item + " Has Been Completed!"
    messages.success(request,(a))
    return redirect('index')

@login_required(login_url='login')
def uncross(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=False
    item.save()
    a= item.item + " Has Been Set to Ongoing!"
    messages.success(request,(a))
    return redirect('index')

@login_required(login_url='login')
def edit(request, item_id):
    if request.method == 'POST':
        item=Item.objects.get(pk=item_id)
        form=ItemForm(request.POST, instance=item)
        user=request.user
        if form.is_valid():
            item.save()
            a = item.item + ' Has Been Successfully Updated!'
            messages.success(request,(a))
            return redirect('index')
        else:
            return redirect('index')

@login_required(login_url='login')
def search(request):
    query=request.GET.get("q")
    if query:
        items=Item.objects.filter(Q(item__icontains=query)|Q(description__icontains=query)).distinct().order_by('-created')
        a= 'Matched Results for ' + query + ' Are Ready'
        messages.success(request,(a))
        return render(request,'index.html', context={'items': items})
    else:
        return redirect('index')

@login_required(login_url='login')
def completed_task(request):
    items=Item.objects.filter(completed=True)
    messages.success(request,('Showing All Completed Task'))
    return render(request,'index.html', context={'items': items})

@login_required(login_url='login')
def ongoing_task(request):
    items=Item.objects.filter(completed=False)
    messages.success(request,('Showing All Ongoing Task'))
    return render(request,'index.html', context={'items': items})

@login_required(login_url='login')
def all_completed(request):
    items=Item.objects.filter(completed=False)
    for item in items:
        item.completed=True
        item.save()
    messages.success(request,('All Tasks are set to Completed'))
    return redirect('index')

@login_required(login_url='login')
def all_ongoing(request):
    items=Item.objects.filter(completed=True)
    for item in items:
        item.completed=False
        item.save()
    messages.success(request,('All Tasks are set to Ongoing'))
    return redirect('index')

@login_required(login_url='login')
def del_completed(request):
    items=Item.objects.filter(completed=True)
    for item in items:
        item.delete()
    messages.success(request,('All Completed Tasks are Deleted'))
    return redirect('index')

@login_required(login_url='login')
def del_all(request):
    items=Item.objects.all()
    for item in items:
        item.delete()
    messages.success(request,('All Tasks are Deleted'))
    return redirect('index')
