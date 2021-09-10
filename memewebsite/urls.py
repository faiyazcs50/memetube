from re import VERBOSE
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="index" ),
    path("memes/<str:page_no>", views.meme_links, name="memelinks"),
    path("shittyposts", views.shittyposts, name="shittyposts"),
    path("shittypost/<str:post_name>", views.shitty_post, name="shittypost")
]