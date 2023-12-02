# users/views.py
from rest_framework import generics, status
from .models import CustomUser
from .serializers import UserSerializer
from subscribes.shortcuts import check_permission, object_is_exist
from rest_framework.response import Response

class UserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk=None):
        can_view = check_permission('view_customuser', request)
        if can_view:
            if pk:
                instance = object_is_exist(pk=pk, model=CustomUser)
                serialzier = UserSerializer(instance)
            else:
                queryset = CustomUser.objects.all()
                serialzier = UserSerializer(queryset, many=True)
            return Response(serialzier.data)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def post(self, request):
        can_post = check_permission('add_customuser', request)
        if can_post:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def put(self, request, pk):
        can_update = check_permission('change_customuser', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=CustomUser)
            serializer = UserSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def patch(self, request, pk):
        can_update = check_permission('change_customuser', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=CustomUser)
            serializer = UserSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def delete(self, request, pk):
        can_delete = check_permission('delete_customuser', request)
        if can_delete:
            instance = object_is_exist(pk=pk, model=CustomUser)
            instance.delete()
            return Response({'Message': 'User has been deleted successfully'})
        else:
            return Response({'Message': 'you do not have access to perform that action'})