from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Function Based View for Displaying Homepage
def home(request):
    return render(request, 'user/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'user/signupuser.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'user/loginuser.html')


def logoutuser(request):
    if request.method == 'POST':
        try:
            del request.session['token']
        except KeyError:
            pass
        try:
            logout(request)
        except KeyError:
            pass

        return redirect('home')


def userdata(request):
    if request.method == 'GET':
        try:
            token = request.session['token']
            return render(request, 'user/list_user.html', {'token': token})
        except:
            return redirect('loginuser')
