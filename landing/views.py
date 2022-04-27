from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from landing.models import Post


def index(request):
    return render(request, "landing/index.html")

def post_create(request):
    if request.method == "GET":
        return render(request,"landing/create.html")
    elif request.method == "POST":
        print(request.POST["title"])
        print(request.POST["content"])
        if request.FILES["image"]:
            print(request.FILES["image"])

        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        if request.FILES.get("image"):
            new_post.head_image = request.FILES["image"]
        new_post.save()
        # return HttpResponseRedirect(reverse("landing:read_all"))
        return redirect("landing:read_all")

def post_read_all(request):
    post_list = Post.objects.all()
    context = {
        "posts":post_list
    }
    return render(request,"landing/read_all.html",context)

def post_read(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request,"landing/read.html", context)

def post_update(request,post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post": post
        }
        return render(request,"landing/update.html",context)
    elif request.method == "POST":
        target_post = Post.objects.get(id=post_id)
        target_post.title = request.POST["title"]
        target_post.content = request.POST["content"]
        target_post.save()
        
    # return HttpResponseRedirect(f"/landing/read/{post_id}")
    return redirect("landing:read", id=post_id)

def post_delete(request,post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context= {
            "post": post
        }
        return render(request,"landing/delete.html",context)
    elif request.method == "POST":
        target_post = Post.objects.get(id= post_id)
        target_post.delete()
        return HttpResponseRedirect("/landing/read-all/")