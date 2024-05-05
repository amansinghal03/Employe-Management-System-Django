from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse
from django.db.models import Q
from .models import Employe,Role,Department 
from . import main,directkeys

# Create your views here.
def index(request):
    return render(request , 'index.html')
    # pass

def all_emp(request):
    emps=Employe.objects.all()
    context={
        'emps':emps
    }
    
    return render(request , 'all_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        # dept_loc=request.POST['dept_loc']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        hire_date=request.POST['hire_date']

        new_emp=Employe(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=hire_date)
        
        new_emp.save()

        return HttpResponse("Add Succefully")

    elif request.method=="GET":
        return render(request , 'add_emp.html')
    else:
        return HttpResponse("Problem")


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_delete=Employe.objects.get(id=emp_id)
            emp_to_delete.delete()
           
            return HttpResponse("Delete Succesfully")
            
            
        except:
            return HttpResponse("Enter Valid Id")


    emps=Employe.objects.all()
    context={
        'emps':emps
    }

    return render(request , 'remove_emp.html',context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        
        emps=Employe.objects.all()

        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
           
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__role=role)

        context={
        'emps':emps
        }
        return render(request , 'all_emp.html',context)
    
    elif request.method=="GET":
        return render(request , 'filter_emp.html')
    else:
        return HttpResponse("Enter Valid Id")

def ml(request):
    ui=main.ml_fun()
    # ap="https://www.google.com/search?q=dinogame&rlz=1C1JJTC_enIN1014IN1014&oq=dinogame&aqs=chrome.0.69i59j69i57j0i271l3j69i60l3.3681j0j7&sourceid=chrome&ie=UTF-8"
    return render(request,"ml.html",{"home_vale":ui})