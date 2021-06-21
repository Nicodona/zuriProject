from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        full_names = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'email exists')
                return redirect('signup')
            elif User.objects.filter(first_name=full_names).exists():
                messages.info(request, 'name  exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken please choose another')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=full_names)
                user.save()
                return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('success')
        else:
            messages.info((request, 'wrong inputs please try again'))
            return redirect('login.html')

    else:
        return render(request, 'login.html')


def success(request):
    return render(request, 'success.html')
