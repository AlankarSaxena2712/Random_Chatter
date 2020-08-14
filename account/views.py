from django.shortcuts import render
from account.models import User
from rest_framework.views import APIView
from account.serializers import UserSerializer
from random_chatter.response import success, failure, update, remove


# Create your views here.

class UserView(APIView):
    def get(self, request, format=None):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return success(serializer)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(serializer)
        return (serializer)


class UserChanges(APIView):
    def get(self, request, pk, format=None):
        obj = User.objects.get(id=pk)
        serializer = UserSerializer(obj)
        return success(serializer)

    def put(self, request, pk, format=None):
        obj = User.objects.get(id=pk)
        serializer = UserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return update(serializer)
        return failure(serializer)

    def delete(self, request, pk, format=None):
        obj = User.objects.get(id=pk)
        obj.delete()
        return remove()
