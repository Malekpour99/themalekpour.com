from django.shortcuts import render


def index_view(request):
    context = {
        "contents": [
            "programming",
            "hiking & nature",
            "books & movies",
            "motivation",
            "mental & physical health",
            "productivity tips",
        ],
        "full_name": "amirhosein malekpour",
    }
    return render(request, "website/index.html", context=context)


def contact_view(request):
    return render(request, "website/contact.html")


def about_view(request):
    return render(request, "website/about.html")
