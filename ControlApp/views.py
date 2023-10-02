from django.shortcuts import render

from . models import Post


def base(request):
    return render(request,'ControlApp/base.html')

def post(request):
    post = Post.objects.all()
    context = {"post": post }
    return render(request,'ControlApp/post.html', context)

def poststr(request,post_id):
    post = Post.objects.get(id=post_id)
    all = post.objects.all()
    
    context = {"all": all}
    return render(request, "ControlApp/poststr.html", context)