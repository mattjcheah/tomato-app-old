from .models import Deadline
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'tracker/tracker.html')


class CountdownListView(generic.ListView):
    model = Deadline
    template_name = 'tracker/countdown.html'
