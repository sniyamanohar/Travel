from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def package(request):
    return render(request,'package.html')
def contact(request):
    return render(request,'contact.html')
def place(request):
    return render(request,'place.html')
def place2(request):
    return render(request,'place2.html')
def place1(request):
    return render(request,'place1.html')
def place3(request):
    return render(request,'place3.html')
def place4(request):
    return render(request,'place4.html')
def place5(request):
    return render(request,'place5.html')
def place6(request):
    return render(request,'place6.html')
def place7(request):
    return render(request,'place7.html')
def index(request):
    return render(request,'index.html')