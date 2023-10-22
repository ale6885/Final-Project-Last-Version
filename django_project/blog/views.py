from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        'author': 'Alessandra',
        'title': 'First Blog Post',
        'content': 'Content for the first post',
        'date_posted': '20/10/2023' 
    },

    {
         'author': 'John',
        'title': 'Second Blog Post',
        'content': 'Content for the second post',
        'date_posted': '21/10/2023' 
    },

        {
        'author': 'Jane',
        'title': 'Third Blog Post',
        'content': 'Content for the third post',
        'date_posted': '22/10/2023' 
    },

        {
        'author': 'Batman',
        'title': 'Fourth Blog Post',
        'content': 'Content for the fourth post',
        'date_posted': '23/10/2023' 
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts 
    }
    return render(request, 'blog/home.html', context)
  
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 