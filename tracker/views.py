from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'tracker/tracker.html')

@login_required
def countdown(request):
    return render(request, 'tracker/countdown.html')
