from django.shortcuts import render, redirect,get_object_or_404
from KhawaDawaApp.forms import KhawadawaForm
from KhawaDawaApp.models import Khawadawa
from django.contrib import messages
import logging
import logging


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = KhawadawaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Form submission successful')
                return redirect('/api/show')
            except:
                pass
    else:
        form = KhawadawaForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Khawadawa .objects.all()
    return render(request, "show.html", {'KhawaDawa': employees})


def edit(request, id):
    employee = Khawadawa .objects.get(id=id)
    return render(request, 'edit.html', {'KhawaDawa': employee})


# def update(request, id):
#     logger = logging.getLogger('django')
#     employee = Khawadawa .objects.get(id=id)
#     form = KhawadawaForm(request.POST, instance=employee)

#     logger.info('before update validation check')

#     if form.is_valid():
#         logger = logging.getLogger('django')
#         logger.info('after validation message')

#         form.save()
#         return redirect('/api/show')
#     return render(request, 'edit.html', {'KhawaDawa': employee})


def destroy(request, id):
    employee = Khawadawa .objects.get(id=id)
    employee.delete()
    return redirect('/api/show')

def update(request, id):
    id = int(id)
    try:
        print("inside try")
        khawa = Khawadawa.objects.get(id = id)

    except Khawadawa.DoesNotExist:
        print("inside except")
        return redirect('/api/show')
    khawa_form = KhawadawaForm(request.POST or None, instance = khawa)
    if khawa_form.is_valid():
       khawa_form.save()
       print("inside  after save")
       return redirect('/api/show')
    return render(request, 'edit.html', {'KhawaDawa': khawa_form})
    