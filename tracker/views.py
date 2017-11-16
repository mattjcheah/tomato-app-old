from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'tracker/tracker.html')


