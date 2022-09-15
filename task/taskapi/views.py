from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serialiser import TaskSerialiser


class TaskAPIView(APIView):
    def get(self, request):
        w = Task.objects.all()
        return Response({'post': TaskSerialiser(w, many=True).data})

    def post(self, request):
        serializer = TaskSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Task.objects.create(
            title=request.data['title'],
            cat_id=request.data['cat_id'],
            content=request.data['content'],
        )
        return Response({'post': TaskSerialiser(post_new).data})
