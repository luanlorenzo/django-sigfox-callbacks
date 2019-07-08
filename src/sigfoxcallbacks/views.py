from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

callback_request = []

@api_view(['POST'])
def sigfox_callback(request):
  if request.method == 'POST':
    callback_request.append(request.data)
  return Response(status=200)

def callbacks_view(request, *args, **kwargs): 
  context = {
    'callbacks': callback_request
  }
  return render(request, "index.html", context)