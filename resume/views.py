from django.shortcuts import render
from resume.models import Contact
# Create your views here.
def index(request):

    

    return render(request,'index.html')

def contact(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        ins=Contact(name=name,email=email,subject=subject,message=message)
        ins.save()
        print("The data has send to db")
    return render(request,'index.html')


