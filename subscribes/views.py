from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Subscribe, SubscribeContract, SubscribeOrder
from .serializers import SubscribeSerializer, SubscribeContractSerializer, SubscribeOrderSerializer
from .shortcuts import check_permission, object_is_exist
from rest_framework_recaptcha.fields import ReCaptchaValidator
from viewclass.settings import DRF_RECAPTCHA_SECRET_KEY

# need to use auth and permissions
class SubscribeView(APIView):
    
    def get(self, request, pk = None):
        if pk:
            instance = object_is_exist(pk=pk, model=Subscribe)
            serialzier = SubscribeSerializer(instance)
        else:
            queryset = Subscribe.objects.all()
            serialzier = SubscribeSerializer(queryset, many=True)
        return Response(serialzier.data)
    
    def post(self, request):
        can_post = check_permission('add_subscribe', request)
        if can_post:
            serializer = SubscribeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message':'you do not have access to perform that action'})

    def put(self, request, pk):
        can_update = check_permission('change_subscribe', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=Subscribe)
            serializer = SubscribeSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message':'you do not have access to perform that action'})
        
    def patch(self, request, pk):
        can_update = check_permission('change_subscribe', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=Subscribe)
            serializer = SubscribeSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message':'you do not have access to perform that action'})

    def delete(self, request, pk):
        can_delete = check_permission('delete_subscribe', request)
        if can_delete:
            instance = object_is_exist(pk=pk, model=Subscribe)
            instance.delete()
            return Response({'Message' : 'subscribe has been deleted successfuly'})
        else:
            return Response({'Message':'you do not have access to perform that action'})


class SubscribeOrderView(APIView):
    def get(self, request, pk=None):
        can_view = check_permission('view_subscribeorder', request)
        if can_view:
            if pk:
                instance = object_is_exist(pk=pk, model=SubscribeOrder)
                serialzier = SubscribeOrderSerializer(instance)
            else:
                queryset = SubscribeOrder.objects.all()
                serialzier = SubscribeOrderSerializer(queryset, many=True)
            return Response(serialzier.data)
        else:
            return Response({'Message':'you do not have access to perform that action'})
    
    def post(self, request):
        serializer = SubscribeOrderSerializer(data=request.data)
        
        if serializer.is_valid():
            # capacha = serializer.validated_data['captcha']
            # capacha_validator = ReCaptchaValidator(secret_key=RECAPTCHA_PRIVATE_KEY)
            # capacha_valid = capacha_validator(capacha)
            # if not capacha_valid:
            #     return Response({'Error':'reCAPTCHA validation failed'})
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def put(self, request, pk):
        can_update = check_permission('change_subscribeorder', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=SubscribeOrder)
            serializer = SubscribeOrderSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message':'you do not have access to perform that action'})

    def patch(self, request, pk):
        can_update = check_permission('change_subscribeorder', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=SubscribeOrder)
            serializer = SubscribeOrderSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message':'you do not have access to perform that action'})
        
    def delete(self, request, pk):
        can_delete = check_permission('delete_subscribeorder', request)
        if can_delete:
            instance = object_is_exist(pk=pk, model=SubscribeOrder)
            instance.delete()
            return Response({'Message' : 'subscribe order has been deleted successfuly'})
        else:
            return Response({'Message':'you do not have access to perform that action'})


# need to use auth and permissions
class SubscribeContractView(APIView):
    def get(self, request, pk=None):
        can_view = check_permission('view_subscribecontract', request)
        if can_view:
            if pk:
                instance = object_is_exist(pk=pk, model=SubscribeContract)
                serialzier = SubscribeContractSerializer(instance)
            else:
                queryset = SubscribeContract.objects.all()
                serialzier = SubscribeContractSerializer(queryset, many=True)
            return Response(serialzier.data)
        else:
            return Response({'Message': 'you do not have access to perform that action'})
    
    def post(self, request):
        can_add = check_permission('add_subscribecontract', request)
        if can_add:
            serializer = SubscribeContractSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def put(self, request, pk):
        can_update = check_permission('change_subscribecontract', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=SubscribeContract)
            serializer = SubscribeContractSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def patch(self, request, pk):
        can_update = check_permission('change_subscribecontract', request)
        if can_update:
            instance = object_is_exist(pk=pk, model=SubscribeContract)
            serializer = SubscribeContractSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message': 'you do not have access to perform that action'})

    def delete(self, request, pk):
        can_delete = check_permission('delete_subscribecontract', request)
        if can_delete:
            instance = object_is_exist(pk=pk, model=SubscribeContract)
            instance.delete()
            return Response({'Message': 'subscribe contract has been deleted successfully'})
        else:
            return Response({'Message': 'you do not have access to perform that action'})