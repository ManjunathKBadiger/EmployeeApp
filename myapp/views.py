from django.shortcuts import render, redirect
from .models import Emplyee
from .forms import EmployeeForm
# Create your views here.


def welcome(request):
    return render(request, "welcome.html")


def load_form(request):
    form = EmployeeForm
    return render(request, 'index.html', {'form': form})


def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    emp = Emplyee.objects.all
    return render(request, 'show.html', {'emp': emp})


def edit(request, id):
    emp = Emplyee.objects.get(id= id)
    return render(request, 'edit.html', {'emp': emp})


def update(request, id):
    emp = Emplyee.objects.get(id= id)
    form = EmployeeForm(request.POST, instance=emp)
    form.save()
    return redirect('/show')


def delete(request, id):
    emp = Emplyee.objects.get(id= id)
    emp.delete()
    return redirect('/show')


def search(request):
    given_name = request.POST['name']
    emp = Emplyee.objects.filter(ename__icontains=given_name)
    return render(request, 'show.html', {'emp': emp})
