from django.shortcuts import render

def index(request):
      return render(request,'cafehub\homepage.html')
     
def login(request):
     return render(request,'cafehub\loginpage.html')
      



