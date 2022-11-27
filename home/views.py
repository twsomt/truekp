from django.shortcuts import render
from home.models import Feed


def index(request):
    return render(request, 'home/index.html')

def feed(request):
    feeds = Feed.objects.all()
    context = {
        'feeds': feeds,
    }

    return render(request, 'home/feed.html', context)