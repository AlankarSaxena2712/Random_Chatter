from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from account.models import User
from .models import Message
from .serializers import MessageSerializer


@api_view(('GET', 'POST',))
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id = sender, receiver_id = receiver)
        serializer = MessageSerializer(messages, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status = 400)
