from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Employee
@login_required

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'epmployees/list.html', {'employees': employees})





def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        salary = request.POST['salary']

        employee=Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary
        )

        messages.success(request, "Employee added successfully!")



        return redirect('employee_list')
    return render(request, 'epmployees/add.html')

def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()
        messages.success(request, "Employee Updated Successfully")
        return redirect('employee_list')

    return render(request, 'epmployees/update.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('employee_list')


def employee_list(request):

    search = request.GET.get('search')

    if search:
        employee_list = Employee.objects.filter(name__icontains=search)
    else:
        employee_list = Employee.objects.all()

    paginator = Paginator(employee_list, 3)

    page_number = request.GET.get('page')

    employees = paginator.get_page(page_number)

    return render(request, 'epmployees/list.html', {'employees': employees})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/employees/')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'epmployees/login.html')


# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'epmployees/register.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')