from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
from trips.models import Post


def hello_world(request):
    return render_to_response('hello_world.html',{'current_time':str(datetime.now())})

def home(request):
    post_list = Post.objects.all()
    return render_to_response('home.html',{'post_list':post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render_to_response('post.html', {'post': post})


