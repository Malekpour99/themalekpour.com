from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag("blog/includes/blog-categories.html")
def post_categories():
    "Retrieving categories and counting how many posts are related to them"
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    return {"categories": cat_dict}