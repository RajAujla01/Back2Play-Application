from django.shortcuts import render, redirect
from .models import WorkoutSession
from django import forms
from django.forms import forms
from account.models import Profile
from workoutsessions.forms import ProfileForm
from django.http import HttpResponseRedirect
from blog.models import BlogPost
from django.utils import timezone
from datetime import datetime
import datetime
import re
from account.models import Profile, MemberLastCompleteHistory
from collections import defaultdict


def workout_sessions(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    workout_sessions = WorkoutSession.objects.all()
    context = {
        'workout_sessions': workout_sessions
    }
    
    profile = request.user.profile
    position = profile.position
    if position > 12:
        return render(request, 'finished.html', context)   

    return render(request, 'workout.html', context)
    

def workout_history_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    workout_sessions = WorkoutSession.objects.all()

    profile = request.user.profile
    position = profile.position

    filtered_workout_sessions = WorkoutSession.objects.all().filter(workout_num__lt=position)

    #GETTING ROUTINES COMPLETED IN A LIST 
    workout_sessions = filtered_workout_sessions
    position = position - 1 
    user_profile = request.user.profile

    #GETTING POSITIONS IN A LIST
    position_list = [f"Session {i}" for i in range(1, user_profile.position)]

    #GETTING DATETIMES INTO A LIST
    history_list = []
    history_instance = MemberLastCompleteHistory.objects.filter(user=user_profile.user).first()
    if history_instance:
        if history_instance.session_complete_1:

            history_instance.session_complete_1 = history_instance.session_complete_1.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_1)

        if history_instance.session_complete_2:

            history_instance.session_complete_2 = history_instance.session_complete_2.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_2)

        if history_instance.session_complete_3:

            history_instance.session_complete_3 = history_instance.session_complete_3.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_3)
    
        if history_instance.session_complete_4:

            history_instance.session_complete_4 = history_instance.session_complete_4.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_4)


        if history_instance.session_complete_5:

            history_instance.session_complete_5 = history_instance.session_complete_5.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_5)

        if history_instance.session_complete_6:

            history_instance.session_complete_6 = history_instance.session_complete_6.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_6)

        if history_instance.session_complete_7:

            history_instance.session_complete_7 = history_instance.session_complete_7.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_7)

        if history_instance.session_complete_8:

            history_instance.session_complete_8 = history_instance.session_complete_8.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_8)

        if history_instance.session_complete_9:

            history_instance.session_complete_9 = history_instance.session_complete_9.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_9)

        if history_instance.session_complete_10:

            history_instance.session_complete_10 = history_instance.session_complete_10.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_10)

        if history_instance.session_complete_11:

            history_instance.session_complete_10 = history_instance.session_complete_11.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_11)

        if history_instance.session_complete_12:

            history_instance.session_complete_12 = history_instance.session_complete_12.strftime("%Y-%m-%d %H:%M:%S")

            history_list.append(history_instance.session_complete_12)


    #combine the two lists in alternating fashion
    combined_list = []
    for i in range(max(len(position_list), len(history_list))):
        if i < len(position_list):
            combined_list.append(position_list[i])
        if i < len(history_list):
            combined_list.append(history_list[i])

    workout_sessions_list = list(workout_sessions.values())

    grouped_workout_sessions = defaultdict(list)
    #Iterate through each workout session in the list
    for session in workout_sessions_list:
        workout_num = session['workout_num']
        grouped_workout_sessions[workout_num].append(session)

        grouped_workout_sessions_list = list(grouped_workout_sessions.values())
    
    position = profile.position
    if position != 1:

        group_history_pairs = list(zip(grouped_workout_sessions_list, history_list))

        context = {
        'workout_sessions': workout_sessions,
        "position":position,
        'combined_list': combined_list,
        'position_list': position_list,
        'history_list': history_list,
        'workout_sessions_list': workout_sessions_list,
        'grouped_workout_sessions_list': grouped_workout_sessions_list,
        'group_history_pairs': group_history_pairs,
        }

        return render(request, 'workouthistory.html', context)

    context = {
        'workout_sessions': workout_sessions,
        "position":position,
        'combined_list': combined_list,
        'position_list': position_list,
        'history_list': history_list,
        'workout_sessions_list': workout_sessions_list,
    }

    return render(request, 'workouthistory.html', context)


def change_position_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    profile = request.user.profile
    position = profile.position

    if request.method == 'POST':
        #update = request.POST.get('change')
        update = request.POST['change']
        profile.position = update
        profile.save()
        
    context = {"position":position}
   
    return render(request, 'changeposition.html', context)

def acwrc_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.method == 'POST':
        week1 = request.POST['week1']
        week2 = request.POST['week2']
        week3 = request.POST['week3']
        week4 = request.POST['week4']
        total = int(week1) + int(week2) + int(week3) + int(week4)   #add up 4 inputs 
        average = total / 4                                         #divide by 4 to get average 
        acwr = int(week4) / average                                 #divide 4th week value by average for ratio value
        context = {"acwr":acwr}                                     #add ratio value to context 

    return render(request, 'acwrcalc.html', context)


def workout_complete_success_view(request):

    context = {}
    if not request.user.is_authenticated:
        return redirect("login")
    
    profile = request.user.profile
    now = datetime.datetime.now()
    member_instance = request.user
    member_instance, created = MemberLastCompleteHistory.objects.get_or_create(user=member_instance)
    member_instance.save()

    profile = request.user.profile
    position = profile.position

    if position == 1:
        member_instance.session_complete_1 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_1
        the_date = timeanddatenow
            
        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)

    if position == 2:
        member_instance.session_complete_2 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_2
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)

    if position == 3:
        member_instance.session_complete_3 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_3
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 4:
        member_instance.session_complete_4 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_4
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 5:
        member_instance.session_complete_5 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_5
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 6:
        member_instance.session_complete_6 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_6
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 7:
        member_instance.session_complete_7 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_7
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 8:
        member_instance.session_complete_8 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_8
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 9:
        member_instance.session_complete_9 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_9
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)
    
    if position == 10:
        member_instance.session_complete_10 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_10
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)

    if position == 11:
        member_instance.session_complete_11 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_11
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        profile.position += 1
        profile.save()

        return render(request, 'workoutsuccess.html', context)  

    if position == 12:
        member_instance.session_complete_12 = now
        member_instance.save()
        timeanddatenow = member_instance.session_complete_12
        the_date = timeanddatenow

        context = {
            'workout_sessions': workout_sessions,
            "the_date":the_date,
            "position":position,
            }

        #profile.position += 1
        profile.save()
        return render(request, 'finished.html', context)  
        #return render(request, 'workoutsuccess.html', context)

      

    profile.position += 1
    profile.save()  

    datenow = now.strftime("%x")
    timenow = now.strftime("%X")

    context = {
        "profile":profile,
        "datenow":datenow,
        "timenow":timenow,
        'workout_sessions': workout_sessions,
        }

    return render(request, 'workoutsuccess.html', context )


def last_workout_completion_date_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("login")
    
    profile = request.user.profile
    updated_position = profile.position
    updated_position = updated_position - 1
    now = datetime.datetime.now()

    datenow = now.strftime("%x")
    timenow = now.strftime("%X")

    context = {
        "profile":profile,
        "updated_position":updated_position,
        "datenow":datenow,
        "timenow":timenow,

    }
    return render(request, 'last_workout_date.html', context )

def finish_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("login")
    
    return render(request, 'finished.html', context )
    

