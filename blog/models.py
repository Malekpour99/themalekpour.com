from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to="blog/", default="blog/default.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField()
    require_login = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
        # ordering applied here is general, not just limited to the admin page
        # you can change your presented class name
        #   using "verbose_name" and "verbose_name_plural"

    def __str__(self):
        return f" {self.title} - {self.id}"

    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
