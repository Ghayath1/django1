from django.shortcuts import render
from.models import Post

# Create your views here.
def post_list(request):
    blog=Post.objects.all()
    return render(request,'post_list.html',{'all_posts':blog})

def post_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post_detail.html',{'single':Post})

def new_post(erquest):
    pass

def edit_post(request,id):
    pass 
def delete_post(request,id):
    pass