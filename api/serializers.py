from dataclasses import fields
from rest_framework import serializers
from blog.models import Post


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
