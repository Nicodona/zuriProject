from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View


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

def logout(request):
    auth.logout(request)
    return redirect('signup')

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                if User.objects.filter(email=email).exists():
                    update = User.objects.get(username=username)
                    update.password = make_password(password)
                    update.save()
                    return redirect('login')
                else:
                    messages.info(request, 'no matchng email related to ' + username + 'please provide a valid email')

                    return redirect('reset_password')

            else:
                messages.info(request, 'we couldn\'t find any username relating to this')
                return redirect('reset_password')

        else:
            messages.info(request, 'password mismatched please repeat')
            return redirect('reset_password')
    else:
        return render(request, 'reset_password.html')


# class RequestPassReset(View):
#     def get(self, request):
#         return render(request, 'reset_password.html')
#
#     def post(self, request):
#         email = request.POST['email']
#         context = {
#             'values': request.POST
#         }
#         if not va