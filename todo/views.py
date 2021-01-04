from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
from .forms import ToDoForm

# Create your views here.

def home(request):
    context = {}
    todos  = Todo.objects.all()
    context['todos'] = todos
    if request.POST:
        form = ToDoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ToDoForm()
            context['form'] = form
    else:
        form = ToDoForm(
            initial={
                'titile': '',
                'description': ''
            }
        )
        context['form'] = form
    return render(request,'home.html', context)
    # return HttpResponse("This is the home page")


def detail_view(request, id):
    context = {}
    todo = Todo.objects.get(id=id)
    context['todo'] = todo
    return render (request, 'details.html', context)

def index_view(request):
    return HttpResponse("This is index page ha ha ha...")


#  RANDOM VIEW
# def get_notifications(request):
#     context = {}
#     user = request.user
#     notifications = Notification.objects.filter(user=user)
#     context['notifications'] = notifications
#     return render (request, 'notifications.html', context)
