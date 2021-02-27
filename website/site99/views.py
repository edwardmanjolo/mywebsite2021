from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'edward',
        'title': 'site99',
        'content': 'new post',
        'date_posted': 'august 2020'

    },
    {
        'author': 'baju',
        'title': 'site99 sure',
        'content': 'new post 2',
        'date_posted': 'september 2020'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'site99/site99-home.html', context)


def about(request):
    return render(request, 'site99/site99-about.html', {'title': 'About'})


def contact(request):
    return render(request, 'site99/site99-contact.html', {'title': 'Contact'})
