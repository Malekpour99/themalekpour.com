from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.db.models import Q
from django.contrib import messages


def home_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)
    page_title = "blog home"
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])
        page_title = "Category: " + kwargs["cat_name"] + " - Posts"
    if kwargs.get("tag_name"):
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])
        page_title = "Tag: " + kwargs["tag_name"] + " - Posts"
    context = {"posts": posts, "page_title": page_title}
    return render(request, "blog/blog.html", context)


def single_view(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your Comment Submitted Successfully. Thanks!",
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Your Comment Didn't Submit! Please try again."
            )

    posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)
    post = get_object_or_404(posts, id=pid)
    # checking if the post requires user to be logged in
    if not post.require_login or request.user.is_authenticated:
        comments = Comment.objects.filter(post=post, approved=True)
        tags = post.tags.all()
        form = CommentForm()
        post.counted_views += 1
        post.save()
        context = {"post": post, "tags": tags, "form": form, "comments": comments}
        return render(request, "blog/blog-single.html", context)
    else:
        return render(request, "blog/blog-single.html", context)


def search_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)
    if request.method == "GET":
        # python "warlus" option ( := ) assign the value to the variable -> less code
        if search_query := request.GET.get("search"):
            posts = posts.filter(
                Q(content__contains=search_query) | Q(title__contains=search_query)
            )
            page_title = "Searched for: " + '"' + search_query + '"'
    context = {"posts": posts, "page_title": page_title}
    return render(request, "blog/blog.html", context)
