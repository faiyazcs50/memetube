from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import meme, shittypost
from django.core.paginator import Paginator
from time import sleep

# Create your views here.
def index(request):
    return render(request, "memewebsite/memes.html")

def meme_links(reuqest, page_no):

    if reuqest.method != "GET":
        return JsonResponse({'message':'GET method required'})

    memes_query = meme.objects.all().order_by("-date")
    pages = Paginator(memes_query, 10)
    memes = []
    memes_list = []
    try:

        page = pages.page(page_no)
    
    except:

        return JsonResponse({'message':'Page not Found'})

    for meme_ in page.object_list:
        memes_list.append(meme_.serialize())
    
    memes.append(memes_list)
    memes.append({'has next':page.has_next()})
    sleep(0.2)
    return JsonResponse(memes,safe=False)

def shittyposts(request):
    return render(request, "memewebsite/shittyposts.html", {
        "shittyposts":shittypost.objects.all()
    })

def shitty_post(request, post_name):
    post = shittypost.objects.get(title = post_name)
    return render(request, "memewebsite/shittypost.html", {
        "shittypost":post
    })