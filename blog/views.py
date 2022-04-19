from django.shortcuts import render
from .models import Post, Catagory
# Create your views here.
from django.contrib import messages


def home(request):
    catagories = Catagory.objects.all()
    post = Post.objects.all()

    return render(request, 'blog/index.html', context={'catagories': catagories, 'posts': post})


def blogDetails(request, slug):
    blog = Post.objects.get(slug=slug)
    return render(request, 'blog/blogdetails.html', context={'post': blog})


def search(request):
    if request.method == 'POST':
        search = request.POST['search_file']
        if search:
            search_file = Post.objects.filter(title__icontains=search)
        else:
            search_file = Post.objects.all()

    context = {'search_file': search_file}
    return render(request, 'blog/search.html', context)
