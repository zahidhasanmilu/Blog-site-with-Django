from django.contrib import admin
from .models import Post, Catagory


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Catagory, CatagoryAdmin)
