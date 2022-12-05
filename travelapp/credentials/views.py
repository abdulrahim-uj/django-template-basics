from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render


def signup(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email_id = request.POST['email']
        pswd = request.POST['password']
        confirm = request.POST['confirm_password']
        if pswd == confirm:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username already taken")
                return redirect('auth:registeruser')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "Email-id already taken")
                return redirect('auth:registeruser')
            else:
                data = User.objects.create_user(username=user_name, email=email_id,
                                                first_name=first_name, last_name=last_name,
                                                password=confirm)
                data.save()
                context = {
                    'messages': "User created, please login with your credentials",
                    'project_name': "Travel App",
                    'title': "Login",
                }
                print(context['messages'])
                return render(request, "credentials/login.html", context=context)
        else:
            messages.info(request, "Password not matched")
            return redirect('auth:registeruser')
    else:
        context = {
            'project_name': "Travel App",
            'title': "Registration",
        }
        return render(request, "credentials/registration.html", context=context)


def signin(request):
    if request.method == 'POST':
        loginusername = request.POST['user_name']
        pswd = request.POST['password']
        user = auth.authenticate(username=loginusername, password=pswd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials!")
            return redirect('auth:loginuser')
    else:
        context = {
            'project_name': "Travel App",
            'title': "Login",
        }
        return render(request, "credentials/login.html", context=context)


def signout(request):
    auth.logout(request)
    return redirect('/')
