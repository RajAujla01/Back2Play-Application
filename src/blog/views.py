from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account

def create_blog_view(request):
    context = {}
    user = request.user                             #only authenticated user can create a blog 
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)  #post request or nothing. File request for images 
    if form.is_valid():
        obj = form.save(commit=False)                                       #create form after fields validated 
                                                                            #set author object to blogpost 
        author = Account.objects.filter(email=user.email).first()          #get first item in queryset 
        obj.author = author                                                 
        obj.save()
        form = CreateBlogPostForm()                                         #reset form 
    context['form'] = form
    return render(request, "blog/create_blog.html", context)

def detail_blog_view(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)          #get the object or give a 404 error 
    context['blog_post'] = blog_post
    return render(request, 'blog/detail_blog.html', context)

def edit_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:                                        #if blog post not made by user 
        return HttpResponse("Sorry but you are not the author of that post!")
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated successfully!"
            blog_post = obj
    form = UpdateBlogPostForm(
        initial = {
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )
    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


def get_blog_queryset(query=None):
    queryset = []                       #empty list 
    queries = query.split(" ")          #splits string into list 
    for q in queries:                   #for item in list 
        posts = BlogPost.objects.filter(
            Q(title__icontains=q)    |      #remove capitalisation 
            Q(body__icontains=q)
        ).distinct()                        #ensure all posts retrieved are unique 
        for post in posts:
             queryset.append(post)      #append list with post 
    return list(set(queryset))

