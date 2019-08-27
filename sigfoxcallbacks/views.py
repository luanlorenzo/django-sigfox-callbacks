from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Callback
from .serializers import CallbackSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'callback': reverse('callback-list', request=request, format=format)
  })

class CallbackList(generics.ListCreateAPIView):
  queryset = Callback.objects.all()
  serializer_class = CallbackSerializer