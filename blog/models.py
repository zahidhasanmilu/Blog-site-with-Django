from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    catagory = models.ForeignKey(
        "Catagory", on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from='title',
                         blank=True, unique=True, null=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_details", kwargs={"slug": self.slug})


class Catagory(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title',
                         blank=True, unique=True,  null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-list", kwargs={"slug": self.slug})
