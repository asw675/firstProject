from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.views import APIView

from first import models
from first.models import user, dishes, evaluation, dishing
from first.serializers import firstSerializer, dishesSerializer, evaluationSerializer, dishingSerializer


class CheckViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = firstSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=['user_id']

class DishesViewSet(viewsets.ModelViewSet):
    queryset = dishes.objects.all()
    serializer_class = dishesSerializer

class evaluationViewSet(viewsets.ModelViewSet):
    queryset = evaluation.objects.all()
    serializer_class = evaluationSerializer

class dishingViewSet(viewsets.ModelViewSet):
    queryset = dishing.objects.all()
    serializer_class = dishingSerializer

class landing(APIView):
    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':None}
        try:
            user=request._request.POST.get('user_name')
            pwd=request._request.POST.get('password')
            obj=models.user.objects.filter(user_name=user,password=pwd).first()
            if not obj:
                ret['code']=1001
                ret['msg']='用户名或密码错误'
            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token']=token
        except Exception as e:
            ret['code']=1002
            ret['msg']='请求异常'

        return JsonResponse(ret)

def md5(user):
    import hashlib
    import time

    ctime=str(time.time())

    m =hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

# Create your views here.
