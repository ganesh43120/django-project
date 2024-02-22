from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.now())
        contact.save()
    
    return render(request,'contact.html')

def servies(request):
    return render(request,"servies.html")

def about(request):
    return render(request,"about.html")

def index(request):
    context={"string1" : "hell0"}
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")
