import json
import sys
import traceback
from rest_framework.response import Response
from rest_framework import viewsets, status, pagination
from rest_framework.decorators import action
from django.shortcuts import render
from django.db.models import Exists, OuterRef, Count, Prefetch
from django.http import JsonResponse,  HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils.urls import replace_query_param
from rest_framework.views import APIView

# models
from negocio_fechado.models import Offer, Tender, Contract, Needs, User

# serializers
from .serializers import (
    OfferSerializer,
    TenderSerializer, 
    ContractSerializer,
    NeedsSerializer,
    UserSerializer
)

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class NeedsViewSet(viewsets.ModelViewSet):
    serializer_class = NeedsSerializer
    queryset = Needs.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class ExemploAPIView(APIView):
    def get(self, request, format=None, uuid=None):
            return Response("Simples View", status=status.HTTP_200_OK)
