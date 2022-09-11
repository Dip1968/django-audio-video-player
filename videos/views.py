from django.shortcuts import redirect, render
from .models import Song,Audio,Thumb
from django.views.decorators.csrf import csrf_exempt
import os
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import ffmpeg_streaming
from ffmpeg_streaming import Formats
from django.http import HttpResponse
import shutil
from .forms import *

# from .forms import GeeksForm
# from .models import thumb

BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    
    context={'songs':Song.objects.all(),'display_images' : Thumb.objects.all() 
}

      
        # getting all the objects of hotel.
    
    return render(request, 'videos/list.html',context)

    
         
    # context={
    #     'songs':Song.objects.all()
    # }
    # return render(request,'videos/list.html',context)

@csrf_exempt
def upload(request):

    if request.method=="POST":
        
        uploaded_file = request.FILES['myFile']
        
        name_array=uploaded_file.name.split('.')
        # name_array2=file.name.split('.')
        uploaded_file.name=name_array[0]
        # file.name=name_array2[0]
        song=Song.objects.create(title=request.POST.get('title'),description=request.POST.get('description'),artist=request.POST.get('artist'),path=f'{uploaded_file.name}')
        song.save()
        song=Song.objects.all().last()
        song_id=song.id
        os.mkdir(f'{BASE_DIR}\\media\\{song_id}\\')
        fs=FileSystemStorage(BASE_DIR)
        fs.save(uploaded_file.name,uploaded_file)
        
        video = ffmpeg_streaming.input(f'{BASE_DIR}\\{uploaded_file.name}')
        dash = video.dash(Formats.h264())
        dash.auto_generate_representations()
        dash.output(f'{BASE_DIR}\\media\\{song_id}\\{uploaded_file.name}.mpd')
        os.remove(f'{BASE_DIR}\\{uploaded_file.name}')
        return redirect('http://127.0.0.1:8000/image/')
        
    return render(request,'videos/upload.html')

       
    # img=Song.objects.get('File')
    # context={'img':img}  
   

@csrf_exempt
def delete_video(request):
    if request.method=="POST":
        song_id=request.POST.get('id')
        song=Song.objects.get(id=song_id)
        song.delete()
        shutil.rmtree(f'{BASE_DIR}\media\{song_id}\\')
        return HttpResponse("Deleted Successfully!")
    return HttpResponse("Method not allowed")

def player(request,id):
    context={
        'song':Song.objects.get(id=id),
        
    }
    return render(request,'videos/watch.html',context)

def audio_player(request):
    context={
        'songs':Audio.objects.all()
    }
    return render(request,'videos/list2.html',context)

@csrf_exempt
def upload_mp3(request):
    if request.method=="POST":
        uploaded_file = request.FILES['myFile']
        audio=Audio.objects.create(title=request.POST.get('title'),artist=request.POST.get('artist'),path=uploaded_file.name)
        audio.save()
        audio=Audio.objects.all().last()
        song_id=audio.id
        fs=FileSystemStorage(f'{BASE_DIR}\\media')
        fs.save(f'{song_id}.mp3',uploaded_file)
        return HttpResponse("Uploaded Successfully!")
    return render(request,'videos/upload_audio.html')

def audio_play_play_by_id(request,id):
    context={
        'song':Audio.objects.get(id=id)
    }
    return render(request,'videos/listen.html',context)

@csrf_exempt
def delete_audio(request):
    if request.method=="POST":
        song_id=request.POST.get('id')
        audio=Audio.objects.get(id=song_id)
        audio.delete()
        os.remove(f'{BASE_DIR}\\media\\{song_id}.mp3')
        return HttpResponse("Deleted Successfully!")
    return HttpResponse("Method not allowed")

def image(request):
      
    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        display_images = Thumb.objects.all() 
    return render(request, 'videos/list.html',
                     {'display_images' : display_images})   

# def display_images(request):
      
#     if request.method == 'GET':
  
#         # getting all the objects of hotel.
#        display_images = Thumb.objects.all() 
#     return render(request, 'videos/list.html',
#                      {'display_images' : display_images})    


# def image(request):
#     user = request.user
#     songs = UserForm(user)

#     if request.method == 'POST':
#         songs = UserForm(request.FILES)
#         if songs.is_valid():
#             songs.save()
#             return redirect('/')

#     return render(request, 'videos/image.html', {'songs': songs})