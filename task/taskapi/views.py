from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Task
from .serialiser import TaskSerialiser


class TaskAPIView(APIView):
    def get(self, request):
        lst = Task.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Task.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

# class TaskAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerialiser

