from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from .forms import PostForm



# Create your views here.

def post_list(request):

    data = Post.objects.all()
    context = {
        'object_list' : data
    }
    return render(request,'posts/post_list.html', context)


def post_details(request,pk):
    data = Post.objects.get(id = pk)
    comments = Comment.objects.filter(post=data)
    context = {
        'post' : data,
        'comments' : comments,

    }

    return render(request,'posts/post_detail.html',context)



def create_post (request) :
    if request.method == 'POST' :
        form = PostForm(request.POST,request.FILES)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else :
        form = PostForm()
    return render (request,'posts/post_form.html', {'form':form})

def edit_post (request,pk) :
    post = Post.objects.get(id=pk)
    if request.method == 'POST' :
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else :
        form = PostForm(instance=post)
    return render (request,'posts/post_edit.html', {'form':form})

def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')













'''



# Class Based View CBV :

class PostList (ListView):
    model = Post


class PostDetail (DetailView):
    model = Post

class AddPost (CreateView) :
    model = Post
    fields = '__all__'
    success_url = '/posts/'

class EditPost (UpdateView) :
    model = Post
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/post_edit.html'

class DeletePost (DeleteView):
    model = Post
    success_url = '/posts/'
    # template_name = 'posts/post_delete.html'


'''