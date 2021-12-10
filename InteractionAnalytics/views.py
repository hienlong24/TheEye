from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from InteractionAnalytics.models import Event


@api_view(['GET', 'POST'])
def event(request):
    if request.method == 'POST':
        d= request.data
        event = Event()
        event.session_id = d['session_id']
        event.category = d['category']
        event.name = d['name']
        event.info = d['data']
        
        event.save()
        return Response(event.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        events = Event.objects.all()
        print(events.__str__())
        return Response(status=status.HTTP_201_CREATED)
