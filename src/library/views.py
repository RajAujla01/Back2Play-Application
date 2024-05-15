from django.shortcuts import render, redirect
from .models import Library
from workoutsessions.models import WorkoutSession
from .forms import VideoForm
# Create your views here.


def library_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    

    vids = Library.objects.all()

    context = {
        "vids":vids
    }
    return render(request, 'library.html', context)


def workoutvid_default_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    workout_sessions = WorkoutSession.objects.all() #store all exercise routines as rows
    vids = Library.objects.all() #store all youtube videos as rows 

    context = {
        'workout_sessions': workout_sessions,
        "vids":vids
    }

    if request.method == 'POST':  #ANYTHING CLICKED TO SUBMIT!
        if 'userchoice' in request.POST: #IF EXERCISE CLICKED
            uservid = request.POST.get('userchoice')   
                                        
            yt_vid = Library.objects.filter(exercise_Title=uservid) 
            url = yt_vid
            context = {
                    'workout_sessions': workout_sessions,
                    "vids":vids,
                    "url":url
                    }
            return render(request, 'govid.html', context)  
        else:
                profile = request.user.profile
                profile.position += 1
                profile.save()                      
            
                return render(request, 'workoutvid.html', context)
                                         
    return render(request, 'workoutvid.html', context)




def go_vid_default_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    workout_sessions = WorkoutSession.objects.all() #store all exercise routines as rows
    vids = Library.objects.all() #store all youtube videos as rows 

    context = {
        'workout_sessions': workout_sessions,
        "vids":vids
    }

    if request.method == 'POST':  #ANYTHING CLICKED TO SUBMIT!
        
        form = VideoForm(request.POST or None)
        if 'userchoice' in request.POST: #if exercise clicked 
            uservid = request.POST.get('userchoice')#get exercise 

            yt_vid = Library.objects.filter(exercise_Title=uservid).values #VidLibrary Lunge
            url = yt_vid                    #VidLibrary Lunge

            context = {         
                        'form':form,
                        'workout_sessions': workout_sessions,
                        "vids":vids,
                        "url":url,
                        "yt_vid":yt_vid,
                        }
                
            form = VideoForm()
                
            return render(request, 'govid.html', context)  
        else:
                    profile = request.user.profile
                    profile.position += 1
                    profile.save()                      
                
                    return render(request, 'workoutvid.html', context)
                                         
        
    return render(request, 'workoutvid.html', context)



    
    
