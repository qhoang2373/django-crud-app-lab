from django.shortcuts import render
from django.http import HttpResponse

# Define the home view function
def home(request):
    return HttpResponse('<h1>Welcome Travelers!</h1>')
    
def about(request):
    return render(request, 'about.html')

def park_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'parks/index.html', {'parks': parks})

class NationalPark:
    def __init__(self, name, location, description, established_date):
        self.name = name
        self.location = location
        self.description = description
        self.established_date = established_date
        
parks = [
    NationalPark('Yosemite', 'California', 'Home of Half Dome', 1890),
    NationalPark('Sequoia', 'California', 'Big Trees', 1890),
]