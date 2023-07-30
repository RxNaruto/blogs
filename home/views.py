from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def home(request):
   return render(request,'home/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            return redirect('/')
    else:
        form = UserRegisterForm()
        return render(request,'home/register.html',{'form': form})
    
def infos(request):
   return render(request,'home/info.html')