from django.shortcuts import render

from .models import Post


# Create your views here.

def post_list(request):

    data = Post.objects.all()
    context = {
        'object' : data
    }
    return render(request,'posts/post_list.html', context)


def post_details(request,pk):
    data = Post.objects.get(id = pk)
    context = {
        'post' : data
    }

    return render(request,'posts/post_detail.html',context)