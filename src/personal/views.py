from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import BlogPost
from blog.views import get_blog_queryset
import datetime
from account.models import MemberLastCompleteHistory
from account.forms import AccountUpdateForm
from django.utils import timezone
from datetime import datetime


BLOG_POST_PER_PAGE = 2


def blog_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')                #get the search terms 
        context['query'] = str(query)
        
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) #sort so newest posts appear at top 

    

    #pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE) #sets how many blogs will appear on page, refers to constant 

    try:
        blog_posts = blog_posts_paginator.page(page)

    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts
    
    return render(request, "bloghome.html", context)

