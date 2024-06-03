from django.urls import path, include
from rest_framework import routers

from core.apps.accounts.api import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]