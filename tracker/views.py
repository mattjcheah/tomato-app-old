from .models import Deadline
from .forms import CountdownForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'tracker/tracker.html')

def countdown(request):
    if request.method == 'POST':
        form = CountdownForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            due = form.cleaned_data['due']
            user = request.user.profile
            Deadline.objects.create(title=title, due=due, user=user)
            
        form = CountdownForm()
    else:
        form = CountdownForm()
    
    return render(
        request, 
        'tracker/countdown.html', 
        {'deadline_list': Deadline.objects.filter(user__exact=request.user.profile), 'form': form}
    )
