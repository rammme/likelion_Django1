from django.shortcuts import render

# Create your views here.

def name(request):
    return render(request, 'name.html')

def index(request):
    userName = request.GET['name']
    return render(request, 'index.html', {'user' : userName})