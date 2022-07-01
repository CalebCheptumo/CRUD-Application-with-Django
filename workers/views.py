from django.shortcuts import render ,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'workers/index.html', {'employees': employees})

def add(request):
    return render(request, 'workers/add.html')

def edit(request, worker_id):
    employee = get_list_or_404(Employee, pk=worker_id)
    return render(request, 'workers/edit.html', {'employee': employee})

def delete(request, worker_id):
    employee = get_list_or_404(Employee, pk=worker_id)
    employee.delete()
    return render(request, '/workers/', {'employee': employee})

def update(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    designation = request.POST['designation']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    age = request.POST['age']
    employee = Employee(first_name=first_name, last_name=last_name, designation=designation, email=email, phone=phone, address=address, city=city, state=state, age=age)
    employee.save()
    return HttpResponseRedirect( '/workers/')

def insert(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    designation = request.POST['designation']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    age = request.POST['age']
    employee = Employee(first_name=first_name, last_name=last_name, designation=designation, email=email, phone=phone, address=address, city=city, state=state, age=age)
    employee.save()
    return HttpResponseRedirect( '/workers/')