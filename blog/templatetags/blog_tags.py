from django import template
from blog.models import Post, Category, Comment
from taggit.models import Tag
from django.utils import timezone

register = template.Library()


@register.simple_tag
def comments_count(pid):
    "Counting the number of comments for the dedicated post"
    return Comment.objects.filter(post=pid, approved=True).count()


@register.inclusion_tag("blog/includes/blog-tags.html")
def all_tags():
    "Retrieving all of the tags"
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag("blog/includes/blog-categories.html")
def post_categories():
    "Retrieving categories and counting how many posts are related to them"
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    return {"categories": cat_dict}


@register.inclusion_tag("blog/includes/blog-recent-posts.html")
def recent_posts(num=5):
    "Retrieving latest posts"
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by(
        "-published_date"
    )[:num]
    return {"posts": posts}
