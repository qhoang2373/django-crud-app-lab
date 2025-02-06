from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import NationalPark
from .forms import TrailForm


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
    park = NationalPark.objects.get(id=park_id)
    trail_form = TrailForm()
    return render(request, 'parks/detail.html', {'park': park, 'trail_form': trail_form})

def add_trail(request, park_id):
    form = TrailForm(request.POST)
    if form.is_valid():
        new_trail = form.save(commit=False)
        new_trail.national_park_id = park_id
        new_trail.save()
    return redirect('park-detail', park_id=park_id)

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

