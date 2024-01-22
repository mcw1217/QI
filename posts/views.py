from django.shortcuts import render,redirect
from posts.models import Post
from django.http import StreamingHttpResponse
from real_time_cap import give_data
import cv2

def feeds(request):
    
    if not request.user.is_authenticated: #요청한 유자가 인증되지 않은경우
        return redirect("/users/login/")
    
    posts= Post.objects.all()
    context={"posts":posts}
        
    return render(request,"posts/feeds.html",context)

def generate_frames():
    while True:
      frame = give_data()
      ret, buffer = cv2.imencode('.jpg',frame)
      if not ret:
        break

      frame = buffer.tobytes()
      yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):

    if not request.user.is_authenticated: #요청한 유자가 인증되지 않은경우
        return redirect("/users/login/")
    
        
    return StreamingHttpResponse(generate_frames(),content_type='multipart/x-mixed-replace; boundary=frame')


