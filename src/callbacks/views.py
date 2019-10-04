from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from .models import Callback
from .serializers import CallbackSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'callback': reverse('get_post_callbacks', request=request, format=format)
    })


@api_view(['GET', 'POST'])
def get_post_callbacks(request):
    # get all callbacks
    if request.method == 'GET':
        callbacks = Callback.objects.all()
        serializer = CallbackSerializer(callbacks, many=True)
        return Response(serializer.data)

    # insert a new callback
    if request.method == 'POST':
        data = {
            'device': request.data.get('device'),
            'snr': request.data.get('snr'),
            'data': request.data.get('data'),
            'time': request.data.get('time')
        }
        serializer = CallbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
