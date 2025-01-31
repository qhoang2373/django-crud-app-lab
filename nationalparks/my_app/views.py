from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import NationalPark

from django.http import HttpResponse

# Define the home view function
def home(request):
    return HttpResponse('<h1>Welcome Travelers!</h1>')
    
def about(request):
    return render(request, 'about.html')

def park_index(request):
    parks = NationalPark.objects.all()
    return render(request, 'parks/index.html', {'parks': parks})

def park_detail(request, park_id):
    parks = NationalPark.objects.all()
    return render(request, 'parks/detail.html', {'parks': parks})

class ParkCreate(CreateView):
    model = NationalPark
    fields = ['name', 'location', 'description', 'established_date']
    success_url = '/parks/'

class ParkUpdate(UpdateView):   
    model = NationalPark
    fields = ['location', 'description', 'established_date']

class ParkDelete(DeleteView):
    model = NationalPark
    success_url = '/parks/'

