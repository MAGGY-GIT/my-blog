from django.shortcuts import render, redirect

from .forms import  RegisterSubscriberForm

from .models import Post

from django.contrib import messages

from django.http import HttpResponse


#function is placed before redirect
#i can use this to say that the survey has been received when client receives survey
#makes changes in base.html and use some javascript
#i can create error messages using messages.error

# Create your views here.

def index(request):

    my_posts = Post.objects.all()
    #this is a query to select our objects

    context = {'posts': my_posts}
    #this allows the records to pass through the dashboard

    return render(request, 'blogposts/index.html', context=context)



def subscribe(request):
    form = RegisterSubscriberForm()

    form_is_valid = False
    if request.method == "POST":
        form = RegisterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            form_is_valid = True


    context = {'form': form, 'form_is_valid': form_is_valid}
    return render(request, 'blogposts/subscribe.html', context=context)

