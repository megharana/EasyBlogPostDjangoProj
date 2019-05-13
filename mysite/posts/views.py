from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def index(request):
    all_obj = Posts.objects.all()[:10]
    context = {'data': 'MySite', 'posts': all_obj}
    return render(request, 'posts/index.html', context)


def details(request, id):
    one_obj = Posts.objects.get(id=id)
    context = {'post': one_obj}
    return render(request, 'posts/details.html', context)
