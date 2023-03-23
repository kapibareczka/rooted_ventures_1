from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Event
from accounts.models import UserProfile


def list(request):
    events = Event.objects.all()
    context = {'event': events}
    print("This is events" + str(events))
    print(context)
    return render(request, 'events/list.html', context)