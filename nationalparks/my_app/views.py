from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NationalPark
from .forms import TrailForm
from .models import Trail


from django.http import HttpResponse

# Define the home view function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('park-index')
        else:
             error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'
    
def about(request):
    return render(request, 'about.html')

@login_required
def park_index(request):
    parks = NationalPark.objects.filter(user=request.user)
    return render(request, 'parks/index.html', {'parks': parks})

@login_required
def park_detail(request, park_id):
    park = NationalPark.objects.get(id=park_id)
    trail_form = TrailForm()
    return render(request, 'parks/detail.html', {'park': park, 'trail_form': trail_form})

@login_required
def add_trail(request, park_id):
    form = TrailForm(request.POST)
    if form.is_valid():
        new_trail = form.save(commit=False)
        new_trail.national_park_id = park_id
        new_trail.save()
    return redirect('park-detail', park_id=park_id)


class ParkCreate(LoginRequiredMixin, CreateView):
    model = NationalPark
    fields = ['name', 'location', 'description', 'established_date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/parks/'

# class TrailList(ListView):
#     model = Trail

class TrailDetail(DetailView):
    model = Trail

class ParkUpdate(UpdateView):   
    model = NationalPark
    fields = ['location', 'description', 'established_date']

class ParkDelete(DeleteView):
    model = NationalPark
    success_url = '/parks/'



class TrailUpdate(LoginRequiredMixin, UpdateView):
    model = Trail
    fields = ['name', 'difficulty']
    success_url = '/trails/' 

class TrailDelete(LoginRequiredMixin, DeleteView):
    model = Trail
    success_url = '/trails/' 

class TrailList(ListView):
    model = Trail
    template_name = 'trails/trail_list.html'  
    context_object_name = 'trails'  


