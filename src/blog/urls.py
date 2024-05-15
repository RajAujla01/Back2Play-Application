from django.urls import path
from blog.views import(
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
)

app_name = 'blog' #reference app name as this urls file is not in mysite directory

urlpatterns = [
    path('create/', create_blog_view, name="create"), #url path for create post 
    path('<slug>/', detail_blog_view, name="detail"), #url path for create post 
    path('<slug>/edit', edit_blog_view, name="edit"), #url path for edit post 
]

