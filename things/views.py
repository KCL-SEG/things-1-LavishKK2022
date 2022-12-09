from django.shortcuts import render
from things import templates

# Create your views here.
def homepage(request):
    return render(request, 'home.html')
