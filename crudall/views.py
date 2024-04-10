from django.shortcuts import render,redirect
from .models import CRUD
from django.contrib import messages
import os

# Create your views here.

# home page
def home(request):
    cr=CRUD.objects.all()
    data={'cr':cr}
    return render(request,'index.html',data)

# Add Data to database 
def create(request):
    if request.method=="POST":
        upload=request.FILES.get('upload')
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        messages.success(request,"CREATE")
        user=CRUD(Image=upload,name=name,price=price,description=description)
        user.save()
        return redirect('home')
    return render(request,'create.html')
# fetch data to database
def update(request,pk):
    crt=CRUD.objects.get(id=pk)
    data={'crt':crt}
    return render(request,'update.html',data)
# Update data 
def to_update(request,pk):
    if request.method=="POST": 
        crt=CRUD.objects.get(id=pk)
        if len(request.FILES) !=0:
            if len(crt.Image)>0:
                os.remove(crt.Image.path)
            crt.Image=request.FILES.get('upload')
        crt.name=request.POST.get('name')
        crt.price=request.POST.get('price')
        crt.description=request.POST.get('description')
        crt.save()
        messages.success(request,"UPDATE")
        return redirect('home')
    return render(request,'update.html')
# Delete data
def delete(request,pk):
    data=CRUD.objects.get(id=pk)
    data.delete()
    messages.success(request,"Delete")
    return redirect('home')