from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from game.views import Game_log,Topic


def user_register(request):
    if(request.method=='POST'):
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if(password1!=password2):
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html', {'title': 'Sign Up'})

        if (User.objects.filter(username=username).exists()):
            messages.error(request, 'Username already exists')
            return render(request, 'register.html', {'title': 'Sign Up'})

        if (User.objects.filter(email=email).exists()):
            messages.error(request, 'Email already registered')
            return render(request, 'register.html', {'title': 'Sign Up'})
        try:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            messages.success(request, 'Sign up successful. Please login to continue')
            return redirect('user:login')
        except Exception as e:
            messages.error(request,'Error: {}'.format(e))
            return render(request, 'register.html', {'title': 'Sign Up'})

    elif (request.method=='GET'):
        return render(request,'register.html',{'title':'Sign Up'})


def user_login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if not username and not password:
            return render(request, 'login.html', {'title': 'Login Page'})

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html', {'title': 'Login Page'})
        try:
            auth.login(request, user)
            messages.success(request, 'You have logged in as {}'.format(user.username))
            return redirect('/')
        except Exception as e:
            messages.error(request, 'Error: {}'.format(e))
            return render(request, 'login.html', {'title': 'Login Page'})
    else:
        return render(request,'login.html',{'title':'Login Page'})


def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('/')


def user_game_history(request):
    user_id = request.user.id
    final_data= []
    history_data= Game_log.objects.filter(user_id=user_id)
    topics= [Topic.objects.get(id=hist.topic) for hist in history_data]
    for i,hist in enumerate(history_data):
        final_data.append({
                    'i': i+1,
                    'topic': topics[i].name,
                    'level': hist.level,
                    'score': hist.score,
                    'date': hist.datetime
        })
    return render(request,'history.html',{'history_data': final_data[::-1]})