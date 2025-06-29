# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet

router = DefaultRouter()
router.register(r'carreras', CarreraViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
