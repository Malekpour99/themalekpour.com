from django.shortcuts import render
from django.utils import timezone
from blog.models import Post


def home_view(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    context = {'posts': posts}
    return render(request, "blog/blog.html", context)


def single_view(request):
    return render(request, "blog/blog-single.html")
