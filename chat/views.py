from django.shortcuts import render, redirect
from .models import Message

def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    return redirect('chatroom')

def chatroom(request):
    chat_messages = Message.objects.all()

    context = {
        'room_name': 'main',
        'chat_messages': chat_messages,
        'current_user': request.user.username
    }

    return render(request, 'chat_room.html', context)
