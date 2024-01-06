from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    date_hierarchy = "created_date"
    # Activates post filtering by date hierarchy
    empty_value_display = "-empty-"
    # Determines how empty values are displayed
    list_display = (
        "title",
        "author",
        "counted_views",
        "status",
        "require_login",
        "published_date",
        "created_date",
    )
    list_filter = ("status", "author")
    # + "fields" can also be used to determine
    #   which fields to display on each data-editing page
    # ordering = ['-created_date'] moved to Meta class
    # Sets the ordering of your data list
    search_fields = ["title", "content"]
    # Determines which fields will be searched for your search query


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = (
        "name",
        "post",
        "approved",
        "created_date",
    )
    list_filter = ("post", "approved")
    search_fields = ["name", "post"]


admin.site.register(Category)
