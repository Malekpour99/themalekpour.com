from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.forms import ContactForm
from django.contrib import messages


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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Ticket Submitted Successfully!")
        else:
            messages.add_message(request, messages.ERROR, "Your Ticket Didn't Submit! Please try again.")
        return HttpResponseRedirect('/')
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


def about_view(request):
    context = {
        "hobbies": [
            {
                "title": "Books & Movies",
                "explanation": "Come on! who can not enjoy a good movie or a good book?!\
                    <br>There's something magical about getting lost in a good story,\
                    whether it's on the page or on the screen.",
            },
            {
                "title": "Music",
                "explanation": "I have specific playlists for different moods; it's \
                    like having a personal therapist in my headphones.<br>Music has \
                        the power to lift my spirits, even on the toughest days.",
            },
            {
                "title": "Sports",
                "explanation": "Literally I am a sports-addict; I train every day \
                    and enjoy endurance sports.<br>Try it and you will see that \
                        training will drastically changes your life!",
            },
            {
                "title": "Mountaineering",
                "explanation": "I have been a nature lover since childhood \
                    and enjoy challenging ascends where I can reach further \
                        from my limits.",
            },
        ],
        "degrees": [
            {
                "title": "Bachelor's degree - Industrial Safety Engineering",
                "explanation": "Graduated from Shahid Beheshti University\
                    <br>GPA: 19.4<br>2017-2021",
            },
            {
                "title": "Post Graduate Diploma - Mathematics & Physics",
                "explanation": "Graduated from National Organization for \
                    Development of Exceptional Talents (SAMPAD)<br>GPA: 19.38<br>2013-2017",
            },
        ],
        "ethics": [
            {
                "title": "Helping Others",
                "explanation": "I would like to help others in every field \
                    that I have experience and also learn from them as well;\
                        sharing is helping.",
            },
            {
                "title": "ISTJ-A - Logistician",
                "explanation": "This means I am a man of my word who put \
                    honesty and loyalty first, prefer to be alone and commited\
                        to my craft.",
            },
            {
                "title": "Never Finished",
                "explanation": "Imporvement and Learning are never finished to me;\
                    no matter what, I always try to improve myself physically \
                        and mentally.<br>even when I reach my goals then I will \
                            look for more bold and challenging ones.",
            },
        ],
        "skills": [
            {
                "icon": "code-s-slash-line",
                "title": "Python & JavaScript",
                "explanation": "These are the core programming languages\
                    I use. I am also experienced in OOP.",
            },
            {
                "icon": "stack-line",
                "title": "Database",
                "explanation": "I 've worked with both SQL and no-SQL \
                    databases like postgresql and mongodb.",
            },
            {
                "icon": "rocket-2-fill",
                "title": "Django",
                "explanation": "I love back-end and Django makes back-end \
                    programming more enjoyable. even for my own website I \
                        have used Django for back-end.",
            },
            {
                "icon": "vuejs-fill",
                "title": "Vue-JS",
                "explanation": "In front-end Development I have worked with \
                    Vue-JS framework and designed pages and components with \
                        this framework and its relevant tools like Vuex, VueRouter and ...",
            },
            {
                "icon": "github-fill",
                "title": "GitHub",
                "explanation": "Everybody knows that life is so \
                    much better when you use Git and GitHub.",
            },
            {
                "icon": "radar-line",
                "title": "Network+",
                "explanation": "Since I am a knowledge enthusiast, \
                    I was curious what is happening in the networks \
                    and how internet works; so I got a Network+ Certificate.",
            },
        ],
    }
    return render(request, "website/about.html", context=context)
