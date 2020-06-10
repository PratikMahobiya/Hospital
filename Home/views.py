from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from .forms import user_Form
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    messages.add_message(request, messages.INFO, 'Welcome to The Hospital Portal.')
    return render(request, 'home/index.html')

def user_regis(request):
	if request.method == "POST":
		form = user_Form(request.POST)
		if form.is_valid():
			try:
				username = request.POST.get('username','')
				email = request.POST.get('email','')
				first_name = request.POST.get('first_name','')
				last_name = request.POST.get('last_name','')
				role = request.POST.get('role','')
				password = request.POST.get('password','')
				form_obj = User(username=username,email=email,first_name=first_name,last_name=last_name,
										role=role,password=password)
				form_obj.save()
				messages.add_message(request, messages.INFO, 'User Successfullly Created..')
				messages.add_message(request, messages.INFO, 'Now You Can Login..')
				return redirect('/login')
			except:
				pass
	else:
		form = user_Form()
	return render(request,'signin.html')

def login(request):
	if request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'You are already Logged in.')
		return HttpResponseRedirect('/home')
	else:
		c = {}
		c.update(csrf(request))
		return render(request, 'login.html', c)
        
def auth_view(request):
	if request.method == "POST":
		username = request.POST.get('user')
		password = request.POST.get('pass')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.add_message(request, messages.INFO, 'Your are now Logged in.')
			return HttpResponseRedirect('/home')
		else:
			messages.add_message(request, messages.WARNING, 'Invalid Login Credentials')
			return HttpResponseRedirect('/login')


def logout(request):
	if request.user.is_authenticated:
		auth.logout(request)
	messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
	messages.add_message(request, messages.INFO, 'Thanks for visiting.')
	return HttpResponseRedirect('/login')
