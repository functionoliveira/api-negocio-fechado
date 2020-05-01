from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

#imports das views
from .views import ( 
    OfferViewSet,
    TenderViewSet,
    ContractViewSet,
    NeedsViewSet,
    UserViewSet, 
    ExemploAPIView
)

router = routers.DefaultRouter()
router.register(r'oferta', OfferViewSet, base_name='oferta')
router.register(r'proposta', TenderViewSet, base_name='proposta')
router.register(r'contrato', ContractViewSet, base_name='contrato')
router.register(r'necessidade', NeedsViewSet, base_name='necessidade')
router.register(r'usuario', UserViewSet, base_name='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('example/', ExemploAPIView.as_view(), name="example"),
    url(r'^admin/', admin.site.urls),
]
