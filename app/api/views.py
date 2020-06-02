import json
import sys
import traceback
from rest_framework.response import Response
from rest_framework import viewsets, status, pagination
from rest_framework.decorators import action
from django.shortcuts import render
from django.db.models import Exists, OuterRef, Count, Prefetch, Q
from django.http import JsonResponse,  HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils.urls import replace_query_param
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

# models
from negocio_fechado.models import Offer, Tender, Contract, Needs, User

# service
from negocio_fechado.services import OfferService, ContractService

# serializers
from .serializers import (
    OfferSerializer,
    TenderSerializer, 
    ReadTenderSerializer,
    ContractSerializer,
    NeedsSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer
)

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(methods=['get'], detail=False, url_path='(?P<offer_pk>.+)/propostas', url_name='propostas_da_oferta')
    def get_tenders_of_offers(self, request, offer_pk=None):
        try:
            tenders = Tender.objects.filter(offer__pk=offer_pk).exclude(state=3)
            serializer = ReadTenderSerializer(tenders, many=True)
            return Response(serializer.data)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['put'], detail=False, url_path='(?P<offer_pk>.+)/proposta/(?P<tender_pk>.+)/aceitar', url_name='aceitar_proposta')
    def accept_tender(self, request, offer_pk=None, tender_pk=None):
        try:
            OfferService.accept_tender(offer_pk, tender_pk)
            return Response(status.HTTP_200_OK)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(methods=['put'], detail=False, url_path='(?P<contract_pk>.+)/contratante/(?P<contractor_pk>.+)/aceitar', url_name='aceitar_contrato')
    def contractor_accept(self, request, contract_pk=None, contractor_pk=None):
        try:
            state = ContractService.contractor_accept_contract(contract_pk, contractor_pk)
            return Response(state, status.HTTP_200_OK)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(methods=['put'], detail=False, url_path='(?P<contract_pk>.+)/contratado/(?P<hired_pk>.+)/aceitar', url_name='aceitar_contrato')
    def hired_accept(self, request, contract_pk=None, hired_pk=None):
        try:
            state = ContractService.hired_accept_contract(contract_pk, hired_pk)
            return Response(state, status.HTTP_200_OK)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NeedsViewSet(viewsets.ModelViewSet):
    serializer_class = NeedsSerializer
    queryset = Needs.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    
    @action(methods=['get'], detail=False, url_path='(?P<needs_pk>.+)/propostas', url_name='propostas_da_necessidade')
    def get_tenders_of_offers(self, request, needs_pk=None):
        try:
            needs = Tender.objects.filter(needs__pk=needs_pk)
            serializer = TenderSerializer(needs, many=True)
            return Response(serializer.data)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(methods=['get'], detail=False, url_path='(?P<user_pk>.+)/contratos', url_name='contratos_do_usuario')
    def get_contracts_by_user(self, request, user_pk=None):
        try:
            contracts = Contract.objects.filter(Q(contractor=user_pk) | Q(hired=user_pk))  
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False, url_path='(?P<user_pk>.+)/propostas', url_name='propostas_do_usuario')
    def get_tenders_by_user(self, request, user_pk=None):
        try:
            tenders = Tender.objects.filter(proposer__pk=user_pk)  
            serializer = TenderSerializer(tenders, many=True)
            return Response(serializer.data)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False, url_path='(?P<user_pk>.+)/ofertas', url_name='ofertas_do_prestador')
    def get_offers_by_user(self, request, user_pk=None):
        try:
            offers = Offer.objects.filter(worker__pk=user_pk)
            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        except Offer.DoesNotExist:
            print(traceback.format_exc())
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False, url_path='(?P<user_pk>.+)/necessidades', url_name='necessidades_do_consumidor')
    def get_needs_by_user(self, request, user_pk=None):
        try:
            needs = Needs.objects.filter(consumer__pk=user_pk)
            serializer = NeedsSerializer(needs, many=True)
            return Response(serializer.data)
        except Needs.DoesNotExist:
            print(traceback.format_exc())
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ExemploAPIView(APIView):
    def get(self, request, format=None, uuid=None):
        return Response("Simples View", status=status.HTTP_200_OK)
