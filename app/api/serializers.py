import json, random, string, time
from rest_framework import serializers
from rest_framework.response import Response
from datetime import datetime, timedelta, timezone, tzinfo
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone, tzinfo

# models
from negocio_fechado.models import Offer, Tender, Contract, Needs, User

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('__all__')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ('__all__')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('__all__')

class NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

