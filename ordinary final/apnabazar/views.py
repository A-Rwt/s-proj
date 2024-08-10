from django.shortcuts import render
from  django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request ,"index.html")

def mytemplate(request):
    return render(request , 'index.html')

def cont(request):
    return render(request,'contact.html') 
  
def breakfast_cofee_tea_sugar(request):
    return render(request,'breakfast.html')  

def fruites(request):
    return render(request,"fruites.html")  

def veggies(request):
    return render(request,'veggies.html')

    
def Staples(request):
    return render(request,'staples.html') 

def chocolate_drinks(request):
    return render(request,'chocolateanddrinks.html') 

def munchies(request):
    return render(request,'munchies.html')  
    
def biscuites(request):
    return render(request,'biscuites.html') 

'''def Masala_oil_&more(request):
    return render(request,'masala.html') '''