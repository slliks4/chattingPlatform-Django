from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from main_Users .models import *
from .models import *
from django.contrib.auth import authenticate,login

def Login(request):
    user_name = 'admin'
    password = 'admin'

    user = authenticate(request, username=user_name, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse('Anonymous User authenticated and logged in successfully!')
    else:
        return HttpResponse('Authentication failed!')

def Index(request):
    if not request.user:
        Login()
    users = User.objects.all()

    context = {
        'users':users,
    }
    return render(request, 'index.html',context)

def Chat_box(request,id):
    if not request.user:
        Login()
    users = User.objects.all()
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=request.user)
    followers = profile.followers.exclude(user=request.user)

    messages = Message.objects.filter((models.Q(sender=request.user) & models.Q(receiver=user)) |
        (models.Q(sender=user) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    context = {
        'followers':followers,
        'users':users,
        'messages':messages,
        'user':user
    }
    return render(request, 'chat_box.html',context)

def Send_message(request,id):
    if not request.user:
        Login()
    users = User.objects.all()
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=request.user)
    followers = profile.followers.exclude(user=request.user)

    messages = Message.objects.filter((models.Q(sender=request.user) & models.Q(receiver=user)) |
        (models.Q(sender=user) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == "POST":
        text = request.POST['message']
        message = Message(sender=request.user, receiver=user, text=text)
        message.save()
        return HttpResponseRedirect(reverse_lazy('send_message',args=[id]))


    context = {
        'followers':followers,
        'users':users,
        'messages':messages,
        'user':user
    }
    return render(request, 'chat_box.html',context)