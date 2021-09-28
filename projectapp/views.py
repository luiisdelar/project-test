from django.shortcuts import render
from projectapp.forms import FormRegisterUser
from .models import *
from django.contrib.auth.models import User
from ipware import get_client_ip
from datetime import datetime   
from time import gmtime, strftime
# Create your views here.

def index(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        ip, is_routable = get_client_ip(request)
        
        user = AnonymousUser.objects.create(ip = ip, created_date = datetime.now())
        return render(request, 'index.html', {'rooms': rooms})
    
            
    
def register(request):
    if request.method == 'GET':
        
        return render(request, 'register.html')

    if request.method == 'POST':
        miFormulario = FormRegisterUser(request.POST)
        
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            
            try:
                user = User.objects.create(
                    username = datos['username'],
                    password = datos['password']
                )
                user_profile = UserProfile.objects.create(
                    #profile_picture = datos['profile_picture'],
                    phone_number = datos['phone_number'],
                    short_description = datos['short_description'],
                    user = user,
                )
                return render(request, 'register.html', {'error': False})
            except:
                return render(request, 'register.html', {'error': True})
            
        else:
                
            return render(request, 'register.html', {'form': miFormulario})
        

def profile(request):

    return render(request, 'profile.html', {'userr': request.user})