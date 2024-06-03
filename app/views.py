from app.models import TODO
from django.contrib.auth.decorators import login_required
from app.forms import TODOForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'home.html', context={'form':form, 'todos':todos})

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        data = {
            'form' : form,
        }
        return render(request, 'login.html', context=data)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request=request, user=user)
                return redirect('home')
        else:
            data = {
            'form' : form,
            }
            return render(request, 'login.html', context=data)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        data = {
            "form" : form,
        }
        return render(request, 'signup.html', context=data)
    
    else:
        form = UserCreationForm(request.POST)
        data = {
            "form" : form,
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=data)

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'home.html', context={'form':form})

def signout(request):
    logout(request=request)
    return redirect('login')

def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')