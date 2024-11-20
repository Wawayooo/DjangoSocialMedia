from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Student


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=usr, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
            #return redirect('stud_records')
        else:
            return HttpResponse("Username and/or password are incorrect. Try again.")

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def addstud(request):
    if request.method == 'POST':
        form = AddStudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewstud')
    else:
        form = AddStudForm()
    return render(request, "addstud.html", {'form': form})  

def viewstud(request):
    students = Student.objects.all()
    return render(request, 'viewstud.html', {'students': students})

def deletestud(request, studentid):
    data = Student.objects.get(studentid=studentid)
    data.delete()
    students = Student.objects.all()
    return render(request, 'viewstud.html', {'students': students})

def editstud(request, studentid):
    data = Student.objects.get(studentid=studentid)
    return render(request, 'editstud.html', {'data': data})

def updatestud(request, studentid):
    data = Student.objects.get(studentid=studentid)
    form = AddStudForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        students = Student.objects.all()
        return render(request, 'viewstud.html', {'students': students})
    else:
        return render(request, 'editstud.html', {'data': data})
    
def stud_records(request):
    return render(request, 'records.html')

def signup_page(request):
    return render(request, 'S_Up.html')

def scroll(request):
    return render(request, 'scroll.html')


