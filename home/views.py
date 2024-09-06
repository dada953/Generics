from django.shortcuts import render
from rest_framework.views import APIView
from home.serilizers import RegisterUser
from rest_framework.response import Response
from rest_framework import generics
from home.models import CustomUser
# Create your views here.
class RegisterView(APIView):
    # serializer_class=RegisterUser
    # queryset = CustomUser.objects.all()


    def post(self,request,format=None):
        seriliz=RegisterUser(data=request.data)
        seriliz.is_valid(raise_exception=True)
        seriliz.save()
        return Response(seriliz.validated_data)