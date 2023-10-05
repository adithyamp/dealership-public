'''def register(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        usern = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']

        if password1 == password2:
            if User.objects.filter(username=usern).exists():
                messages.info(request, 'Username already exists!')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=usern, password=password1, email=email,  first_name=fn, last_name=ln)
                user.save();
                print('Successfully created user!')
                return redirect('accounts:login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('accounts:register')
        return redirect('home:index')
    
    else:
       return render(request, 'register.html')


def login1(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username=uname, password=pswd)

        if user is not None:
            auth.login(request, user)
            return redirect('home:index')
        else:
            messages.info(request, 'Invalid login credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'login.html')


def logout1(request):
    auth.logout(request)
    return redirect('accounts:login')'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.contrib.auth.models import User, auth
from django.urls import conf

from .models import Message
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def inbox(request):
    user = request.user
    messages1 = Message.get_messages(user=user)
    active_direct = None
    directs = None

    if messages1:
        message = messages1[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=user, recipient=message['user']).order_by('-date')
        directs.update(is_read=True)

        for message in messages1:
            if message['user'].username == active_direct:
                message['unread'] = 0
        
    context = {
        'directs': directs,
        'messages1': messages1,
        'active_direct': active_direct,
    }
    
    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))


@login_required
def Directs(request, username):
    user = request.user
    messages1 = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)

    for message in messages1:
        if message['user'].username == username:
            message['unread'] = 0
    
    context = {
        'directs': directs,
        'messages1': messages1,
        'active_direct': active_direct,
    }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))


@login_required
def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        Message.send_message(from_user, to_user, body)
        return redirect('accounts:inbox')
    else:
        HttpResponseBadRequest() 


@login_required
def UserSearch(request):
    query = request.GET.get('q')
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        #pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }
    
    template = loader.get_template('direct/search_user.html')

    return HttpResponse(template.render(context, request))


@login_required
def NewConversation(request, username):
    from_user = request.user
    body = 'Says Hello !'

    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('accounts:usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('accounts:inbox')


def checkDirects(request):
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message.objects.filter(user=request.user, is_read=False).count()

    return {'directs_count': directs_count}

