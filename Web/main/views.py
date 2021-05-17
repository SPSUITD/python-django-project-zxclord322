from django.shortcuts import render
from django.shortcuts import redirect, render
from . forms import UserRegister, UserLogin
from django.contrib.auth import login as auth_login, logout as logoutuser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from . models import Room, Message
from .forms import FormCreate
from django.http import HttpResponse, JsonResponse




def Createroom(request):
    room = Room.objects.order_by('pk')
    form = FormCreate(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'createroom.html', {'room':room,'form':form})


class RoomView(ListView):
    template_name = 'createroom.html'
    context_object_name = 'room'
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context.update({
            'room': Room.objects.order_by('pk'),
            
        })
        return context

    def get_queryset(self):
        return Room.objects.order_by('pk')


def home(request):
    lis = range(5, 11)
    cats = range(8, 11)
    return render(request, 'index.html', {'lis': lis,'cats':cats })


def rooms(request):
    return render(request, 'createroom.html')


class UserView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'Users'
    ordering = ['-last_login']

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,

    })

def checkview(request):
    room = request.POST['room_name']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
    


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegister()
        messages.error(request, 'Registration error')

    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserLogin()
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html', {'form': form, })

def suport(request):
    return render(request, 'suport.html')


def logout(request):
    logoutuser(request)
    return redirect('/login')
