from django.shortcuts import render
from .models import Post, Catagory
# Create your views here.


def home(request):
    catagories = Catagory.objects.all()
    post = Post.objects.all()

    return render(request, 'blog/index.html', context={'catagories': catagories, 'posts': post})


def blogDetails(request, slug):
    blog = Post.objects.get(slug=slug)
    return render(request, 'blog/blogdetails.html', context={'post': blog})
