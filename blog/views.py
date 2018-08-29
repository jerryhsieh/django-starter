from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from .models import Post

posts = Post.objects.all()[:10]

context = {
    'title': 'Latest Posts',
    'posts': posts
}


def index(request):
    #    return HttpResponse('Hello from Blog')
    print(posts)
    return render(request, 'blog/index.html', context)


def details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/details.html', context)
