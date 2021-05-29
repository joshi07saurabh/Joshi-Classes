from django.shortcuts import render
from JoshiClasses.models import Home
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        address = request.POST.get("address")
        home = Home(name=name,email=email,phone=phone,subject=subject,address=address)
        home.save()
        
    return render(request,"home.html")
    
