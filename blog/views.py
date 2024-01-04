from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


def home_view(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    context = {'posts': posts}
    return render(request, "blog/blog.html", context)


def single_view(request, pid):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    post = get_object_or_404(posts, id=pid)
    # checking if the post requires user to be logged in
    if not post.require_login or request.user.is_authenticated:
        # post = get_object_or_404(Post, id=pid) # this is unsafe because you can access not published posts by using ID
        post.counted_views += 1
        post.save()
        tags = post.tags.all()
        context = {'post': post, 'tags': tags }
        return render(request, "blog/blog-single.html", context)
    else:
        return render(request, "blog/blog-single.html", context)
