"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from personal.views import (
    blog_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
    initialise_user_view,
    

    
)

from workoutsessions.views import (
    workout_sessions, 
    workout_history_view, 
    change_position_view, 
    acwrc_view,
    last_workout_completion_date_view,
    workout_complete_success_view,
    finish_view,
)

from library.views import (
    library_view,
    workoutvid_default_view,
    go_vid_default_view,
    
)


urlpatterns = [
    path('', account_view, name="home"),
    path('admin/', admin.site.urls),
    path('account/', account_view, name="account"),
    path('blog/', include('blog.urls', 'blog')),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, 
    name="register"),
    path('workout/', workout_sessions, name="workout"),
    path('workouthistory/', workout_history_view, name="workouthistory"),
    path('changeposition/', change_position_view, name="changeposition"),
    path('bloghome/', blog_view, name="bloghome"),
    path('acwrcalc/', acwrc_view, name="acwrcalc"),
    path('library/', library_view, name="library"),
    path('workoutvid/', workoutvid_default_view, name="workoutvid"),
    path('govid/', go_vid_default_view, name="govid"),
    path('initialiseuser/', initialise_user_view, name="initialiseuser"),
    path('workoutsuccess/', workout_complete_success_view, name="workoutsuccess"),
    path('last_workout_date/', last_workout_completion_date_view, name="lastworkoutdate"),
    path('finished/', finish_view, name="finished"),
    


   
    #password reset links
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG: #if in debug mode 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  #add directories to url patterns 

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   

