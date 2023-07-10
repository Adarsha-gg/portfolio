from django.shortcuts import render, HttpResponse
from nav.models import Contact
# Create your views here.
def index(request):
    hero = {'name': 'adu', 
            'bro': 'bro2'}
    return render(request, 'index.html',hero)

def aboutme(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contactme(request):
    if request.method =="POST":
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        email = request.POST['Email']
        message = request.POST['Message']
        ins = Contact(fname=fname, lname=lname, message= message, email= email)
        ins.save()
        print(message)
    return render(request, 'contact.html')