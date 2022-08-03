from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "Not what you think"},
    {"id": 2, "name": "Oh nameee?"},
    {"id": 3, "name": "You really want name?"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for r in rooms:
        if r["id"] == int(pk):
            room = r
    context = {"room": room}
    return render(request, "base/room.html", context)
