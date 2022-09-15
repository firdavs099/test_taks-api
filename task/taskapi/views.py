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
        serializer.save()

        # post_new = Task.objects.create(
        #     title=request.data['title'],
        #     cat_id=request.data['cat_id'],
        #     content=request.data['content'],
        # )
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT does not exists"})

        serializer = TaskSerialiser(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            serializer = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT does not exists"})
        serializer.delete()
        return Response({"post": "delete post" + str(pk)})