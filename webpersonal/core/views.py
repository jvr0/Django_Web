from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request, "core/home.html")
    
def contact(request):
    return render(request, "core/contact.html")

def skills(request):
    return render(request, "core/skills.html")