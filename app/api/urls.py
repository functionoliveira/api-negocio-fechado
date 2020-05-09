from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

#imports das views
from .views import ( 
    OfferViewSet,
    TenderViewSet,
    ContractViewSet,
    NeedsViewSet,
    UserViewSet, 
    ExemploAPIView,
    CustomTokenObtainPairView
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
    path('auth/credentials/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^admin/', admin.site.urls),
]
