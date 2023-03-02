from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
import os
from home.models import Prints
from datetime import datetime
from django.contrib import messages
from home.forms import NewUserForm
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    
def loginuser(request):
    if request.method == 'POST':

        user=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=user,password=password)

        if user is not None:
            #authenticate
            login(request,user)
            return redirect('/')

        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')


#def printout(request):
#   return render(request, 'printout.html')

def printout(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        pdf=request.POST.get('pdf')
        desc=request.POST.get('desc')
        freq=request.POST.get('freq')
        #if freq == None:
        #    messages.success(request, "select number of prints")
        #    return redirect('/printout')
        spiral=request.POST.get('spiral')
        if spiral=='on':
            spiral=True
        else:
            spiral=False
        printobj=Prints(name=name,phone=phone ,email=email, desc=desc, pdf=pdf, freq=freq,spiral=spiral, date=datetime.today())
        printobj.save()
        messages.success(request, "Your request has been sent")
    return render(request, os.path.join('printout.html'))
    #return HttpResponse("Upload your pdf and get the print ")

def redcanteen(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, os.path.join('redcanteen.html'))


def yellowcanteen(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, os.path.join('yellowcanteen.html'))


def restaurant(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, os.path.join('restaurant.html'))



def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})


def register(request):
    if request.method=="POST":
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        username=request.POST.get("username")
        name=request.POST.get("fullname")
        #print(pass1)
        #print(username)
        #print(name)
        if pass1 == pass2:
            user = User.objects.create_user(username=username,email=username, password=pass1)
            user.save()        
    return render(request, 'register.html')


def profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    username=None
    if request.user.is_authenticated:
        username=request.user.username
    print(username)
    print("testing")
    dictt={'uname':username, 'mail':username}
    return render(request, 'profile.html', dictt)


def contact(request):
    return render(request, "contact.html")