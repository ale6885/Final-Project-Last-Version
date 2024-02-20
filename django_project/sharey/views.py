from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView # New import added here
)
from django.http import HttpResponse
from .models import Post

from django.shortcuts import render
import requests

# Create your views here.x
def home(request):
    context = {
       'advert': Post.objects.all()
    }
    return render(request, 'sharey/home.html', context)

class PostlistView(ListView):
    model = Post
    template_name = 'sharey/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'advert'
    ordering = ['-date_posted'] 

class PostDetailView(DetailView):
    model = Post  
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/" # Here we are redirecting the user back to the homepage after deleting a Post successfully
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'sharey/about.html', {'title': 'About'})


def current_weather(request):
    api_key = 'YOUR_WEATHER_API_KEY'
    city = request.GET.get('city')  # Assuming the city name is passed as a query parameter
    url = f'https://api.openweathermap.org/data/2.5/weather?q={Amsterdam}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return render(request, 'weather/current_weather.html', {'weather_data': data})

def forecast(request):
    api_key = 'YOUR_WEATHER_API_KEY'
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={Amsterdam}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return render(request, 'weather/forecast.html', {'forecast_data': data})