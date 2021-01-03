from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

def home(request):
    todos  = Todo.objects.all()
    # todos  = Todo.objects.filter(date_added="")
    context = {}
    context['todos'] = todos
    return render(request,'home.html', context)
    # return HttpResponse("This is the home page")

def index_view(request):
    return HttpResponse("This is index page ha ha ha...")


#  RANDOM VIEW
# def get_notifications(request):
#     context = {}
#     user = request.user
#     notifications = Notification.objects.filter(user=user)
#     context['notifications'] = notifications
#     return render (request, 'notifications.html', context)
