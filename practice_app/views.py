from django.shortcuts import render

# Create your views here.

def app_home(request):
    return render(request, 'app_home.html')