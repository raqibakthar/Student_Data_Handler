from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
@never_cache
def loginfnc(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':

            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'INVALID USER NAME OR PASSWORD')

    return render(request,'login.html')

def logoutfnc(request):
    logout(request)
    return redirect('login')