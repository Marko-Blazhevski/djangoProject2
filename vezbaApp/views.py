from django.shortcuts import render
from vezbaApp.models import *
from vezbaApp.forms import *


# Create your views here.

def index(request):
    return render(request, "index.html")


def posts(request):
    queryset = Post.objects.filter(author=request.user).all()
    context = {"posts": queryset, "form": PostForm}
    return render(request, "posts.html", context=context)
