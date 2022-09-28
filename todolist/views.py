from django.shortcuts import render
import datetime
from todolist.models import Task
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
    'todolist' : data,
    'username' :  request.user.username,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) ## cek ini
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def membuat_task(request):
    if request.method == 'POST':
        title = request.POST.get('todo')
        user = request.user
        # status = False
        description = request.POST.get('description')
        date = datetime.datetime.now()
        # user = request.user
        # status = False
        Task.objects.create(title=title, description=description, date=date, user=user)
        # Task.objects.create(title=title, description=description, date=date, user=user, status=status) ## ini kalo udh ada bomus
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response

    return render(request, "task.html")

def delete(request, pk):
    data = Task.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def status(request, pk):
    data = Task.objects.get(id=pk)
    if data.status == False:
        data.status = True
    else:
        data.status = False
    data.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))