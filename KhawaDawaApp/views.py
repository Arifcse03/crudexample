from django.shortcuts import render, redirect  
from KhawaDawaApp.forms import KhawadawaForm  
from KhawaDawaApp.models import Khawadawa 
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = KhawadawaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/api/show')  
            except:  
                pass  
    else:  
        form = KhawadawaForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Khawadawa .objects.all()  
    return render(request,"show.html",{'KhawaDawa':employees})  
def edit(request, id):  
    employee = Khawadawa .objects.get(id=id)  
    return render(request,'edit.html', {'KhawaDawa':employee})  
def update(request, id):  
    employee = Khawadawa .objects.get(id=id)  
    form = KhawadawaForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect('/api/show') 
    return render(request, 'edit.html', {'KhawaDawa': employee})  
def destroy(request, id):  
    employee = Khawadawa .objects.get(id=id)  
    employee.delete()  
    return redirect('/api/show') 
