from django.shortcuts import render ,get_list_or_404
from django.http import HttpResponse
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
    return render(request, 'workers/delete.html', {'employee': employee})

def insert(request):
    return render(request, 'workers/insert.html')

def update(request, worker_id):
    employee = get_list_or_404(Employee, pk=worker_id)
    return render(request, 'workers/update.html', {'employee': employee})
