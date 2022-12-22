from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from calc.models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')
def Home(request):
   # return HttpResponse("This is home page");
    return render(request,'home.html')
def about(request):
    #return HttpResponse("This is about page");
    return render(request,'about.html')
def services(request):
   # return HttpResponse("This is services page");
     return render(request,'services.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name='name', email='email', phone='phone', desc='desc', date=datetime.today())
        contact.save()
    #return HttpResponse("This is contacts page");
    return render(request,'contact.html')

