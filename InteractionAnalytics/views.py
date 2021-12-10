from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from InteractionAnalytics.models import Event
from datetime import datetime

event_list = [] # list of events recieved in event request
count = 0 # keeps track of how many items in event_list
batch_size = 100 # number of events to be processed

@api_view(['GET', 'POST'])
def event(request):

    global count
    global event_list
    global batch_size

    if request.method == 'POST':
        d= request.data
        event = Event()
        event.session_id = d['session_id']
        event.category = d['category']
        event.name = d['name']
        event.info = d['data']
        time = d['timestamp']
        event.time = datetime.fromisoformat(time)

        event_list.append(event)
        count += 1

        if count == batch_size:
            events = Event.objects.bulk_create(event_list, batch_size )
            count = 0
            event_list = []
            
        return Response(events, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        events = Event.objects.all()
        return Response(events, status=status.HTTP_201_CREATED)
