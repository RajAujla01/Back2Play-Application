from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, ProfileForm
from blog.models import BlogPost
from account.models import Account, Profile, MemberLastCompleteHistory
from django.contrib.auth.decorators import login_required
from .models import Profile
import datetime
from django.utils import timezone
from datetime import datetime
import re

def registration_view(request):
    context = {}
    if request.POST:                            #if post request set the form 
        form = RegistrationForm(request.POST)

        if form.is_valid():                     #if no errors in form 
            form.save()
            email = form.cleaned_data.get('email')  #get email from valid form 
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password) #authenticate the account for the user 
            login(request, account)                                     #log the user in 

   
            if not request.user.is_authenticated:                   #if the user is not authenticated redirect to login page 
                return redirect("login")                          

            return redirect('initialiseuser')
        else:                                           #if form is not validf 
            context['registration_form'] = form         #pass form to template via context to show errors 

    else: #GET request
        form = RegistrationForm()                       #show empty form as user visiting page for first time 
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)             #is user is authenticated, take request, log them out and redirect to homepage 
    return redirect('home')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")                         #redirect home if user authenticated 
    
    if request.POST:    
        form = AccountAuthenticationForm(request.POST)  #account form
        if form.is_valid():
            email = request.POST['email']                   #retrieve email and password values from form 
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)                #log user in 
                return redirect("home")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}    

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user) #form to update account 
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Successfully updated your account details!"
    else:
        form = AccountUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username
                }
            )
    
    lastlogin = request.user.last_login         #store last log in and date joined as variables 
    date_joined = request.user.date_joined

    now = datetime.now()                        #stores current datetime as variable 

    context['date_joined']= date_joined         #add to context dictionary 
    context['lastlogin']= lastlogin

    year = lastlogin.year
    month = lastlogin.month
    day = lastlogin.day
    time = lastlogin.time

    context['year']= year
    context['month']= month
    context['day']= day
    context['time']= time

    datenow = now.strftime("%x")
    timenow = now.strftime("%X")

    difference = lastlogin - date_joined
    difference = str(difference.days)

    context['difference']= difference
 
    context['datenow']= datenow
    context['timenow']= timenow

    user = request.user

    try:
        #retrieve the MemberLastCompleteHistory instance for the user
        user_history_instance = MemberLastCompleteHistory.objects.get(user=user)
        
        latest_value = None
        latest_datetime = None
        
        #list of session_complete field names
        session_complete_fields = [f'session_complete_{i}' for i in range(1, 11)]
        
        #iterate through the fields and find the latest value
        for field_name in session_complete_fields:
            value = getattr(user_history_instance, field_name) #gets value specified by field_name from user_history_instance 
            if value and (latest_datetime is None or value > latest_datetime): #checks if value is more recent 
                latest_value = value
                latest_datetime = value

                now_datetime = timezone.now()
                
                absoluterest = now_datetime - latest_value 
              
                days = absoluterest.days
                hours, seconds = divmod(absoluterest.seconds, 3600)
                minutes, seconds = divmod(seconds, 60)

                time_difference_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds" #format time into readable string

                if days < 0:

                    time_difference_str = f"{hours} hours, {minutes} minutes, {seconds} seconds"

        context['latest_value']= latest_value
        context['absoluterest']= absoluterest
        context['time_difference_str']= time_difference_str
        context['now_datetime']= now_datetime

    except MemberLastCompleteHistory.DoesNotExist:
        context = {
            'latest_value': None
        }
        context['latest_value']= None

    try:
        #retrieve the last MemberLastCompleteHistory instance for the user
        last_history_instance = MemberLastCompleteHistory.objects.filter(user=user).latest('id')
     
       #check for the last session_complete field with a value
        last_session_complete = None
        session_complete_fields = [f'session_complete_{i}' for i in range(1, 11)] #iterate through all 10 rows
        for field_name in session_complete_fields[::-1]:
            value = getattr(last_history_instance, field_name)
            if value:
                last_session_complete = value
                break

        context['last_session_complete'] = last_session_complete

        current_datetime = timezone.now()
        time_difference = current_datetime - last_session_complete

        days = time_difference.days
        seconds = time_difference.seconds

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        rest = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

        wait = 24 - int(hours), int(minutes)

        hourswait = wait[0]
        minswait = wait[1]
        context['wait']= wait
        context['hourswait']= hourswait
        context['minswait']= minswait

        context['rest'] = rest
        
    except MemberLastCompleteHistory.DoesNotExist:
        context = {
            'last_session_complete': None,
        }
        context['last_session_complete'] = None
        context['rest'] = None

    user_id = request.user.id

    try:
        member_history = MemberLastCompleteHistory.objects.get(user_id=user_id)
    except MemberLastCompleteHistory.DoesNotExist:
        member_history = None

    if member_history:
        #check if any of the session_complete_X fields are not empty
        #any checks if value is not None
        has_completed_sessions = any(getattr(member_history, f'session_complete_{i}', None) for i in range(1, 11)) 

        context['user']= member_history.user
        context['has_completed_sessions']= has_completed_sessions

        current_datetime = timezone.now()
        time_difference = current_datetime - last_session_complete

        days = time_difference.days
        seconds = time_difference.seconds

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        rest = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

        wait = 24 - int(hours), int(minutes)

        hourswait = wait[0]
        minswait = wait[1]
        context['wait']= wait
        context['hourswait']= hourswait
        context['minswait']= minswait

        context['rest'] = rest

        if days < 0:
            ready_or_not = (f"Please wait at least 24 hours before exercising again.")

            context['ready_or_not']= ready_or_not

        context['account_form']= form

        blog_posts = BlogPost.objects.filter(author=request.user) #look for blog posts where author is user 
        context['blog_posts'] = blog_posts                          #add user's blogposts to context 

        return render(request, 'account/account.html', context)

    else:
        context['user']= None
        context['has_completed_sessions']= False
        
    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})


@login_required
def initialise_user_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    user_instance = request.user

    profile_instance = Profile.objects.create(user=user_instance, position=1) #set position to 1 to initialise user for routines 
    return redirect('home')  
    


