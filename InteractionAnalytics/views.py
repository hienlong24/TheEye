from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from InteractionAnalytics.models import Event

@api_view(['GET', 'POST'])
def event(request):
    if request.method == 'POST':
        event = request.data
        print(event)
        event = Event(data=request.data)
        if event.is_valid():
            event.save()
            return Response(event.data, status=status.HTTP_201_CREATED)
        return Response(event.errors, status=status.HTTP_400_BAD_REQUEST)
        