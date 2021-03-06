from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logout_view(request):
    """注销"""
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    """注册"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
