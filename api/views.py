from urllib import request
from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializer

# Create your views here.

# Read_all


@api_view(['get'])
def all_blogs(request):
    blogs = Post.objects.all()
    serialized = Postserializer(blogs, many=True)
    return Response({'status': 200, 'payload': serialized.data})


# Read Single
@api_view(['get'])
def single_blog(request, id):
    try:
        blog = Post.objects.get(id=id)
        serialized = Postserializer(blog)
        return Response({'status': 200, 'payload': serialized.data})
    except:
        return Response({'payload': 'Blog Not Found'})


def delete_blog(request, id):
    try:
        blog = Post.objects.get(id=id)
        if blog.delete():
            return HttpResponse('Your Selected Blog Delete')
    except:
        return HttpResponse('Blog is not found')


# Update
@api_view(['POST'])
def update_blog(request, id):
    try:
        blog_data = Post.objects.get(id=id)
        serialized = Postserializer(
            instance=blog_data, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response("Student Information Update")
    except:

        return HttpResponse('Student Not Found')

# Create


@api_view(['POST'])
def create_blog(request):
    try:
        data = request.data
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("New Blog Created")
        return Response('Invalid Information')
    except:
        return Response('Invalid Information')
