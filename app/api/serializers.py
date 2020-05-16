import json, random, string, time, traceback
from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime, timedelta, timezone, tzinfo
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone, tzinfo
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

# models
from negocio_fechado.models import Offer, Tender, Contract, Needs, User

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('__all__')

class ProposerSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'full_name', 'cpf', 'type', 'email')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ('__all__')

class ReadTenderSerializer(serializers.ModelSerializer):
    proposer = ProposerSerializer(read_only=True)

    class Meta:
        model = Tender
        fields = ('__all__')

class NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('__all__')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data): 
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class ContractSerializer(serializers.ModelSerializer):
    tender = TenderSerializer()
    hired = ProposerSerializer()
    contractor = ProposerSerializer()

    class Meta:
        model = Contract
        fields = ('__all__')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
        Classe que extende a classe padrão de serialização de token da lib utilizada para autenticacao jwt (simplejwt),
        para customizações do token.
    """
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except KeyError:
            print(traceback.format_exc()) 
        except Exception as ex:
            print(traceback.format_exc())
            raise exceptions.AuthenticationFailed(
                str(ex),
                'no_active_account'
            )   

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Passando informações do usuário para o toke
        serializer = UserSerializer(user)
        token['user_id'] = serializer.data['id']
        token['email'] = serializer.data['email']
        token['full_name'] = serializer.data['full_name']
        token['photo'] = serializer.data['photo']
        token['birth_date'] = serializer.data['birth_date']
        token['cpf'] = serializer.data['cpf']
        token['type'] = serializer.data['type']
        return token
