from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method =="POST":
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['contact']
            subject = request.POST['subject']
            message = request.POST['message']
            if fname=="" or lname == "" or email == "" or contact == "" or subject == "" or message == "":
                messages.error(request,'All fields are Required.') 
            else:
                val = Contact(fname = fname, lname = lname, email = email, phone = contact, subject = subject, message = message)
                val.save()
                messages.success(request, 'Message send successfully, we will connect to you soon')
        except:
            messages.error(request, 'Some error happened, please try again later.')
    return render(request, 'home/index.html')

def apply(request):
    if request.method =="POST":
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['phone']
            course = request.POST['course']
            branch = request.POST['branch']
            year = request.POST['year']
            if fname=="" or lname == "" or email == "" or contact == "":
                messages.error(request,'Please fill all the required fields.') 
            else:
                val = Member(fname = fname, lname = lname, email = email, phone = contact, branch = branch, course = course, year = year)
                val.save()
                messages.success(request, 'Message send successfully, we will connect to you soon')
        except:
            messages.error(request, 'Some error happened, please try again later.')
    return render(request, 'home/apply.html')