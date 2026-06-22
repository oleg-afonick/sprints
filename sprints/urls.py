from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from pereval.views import PerevalViewSet

router = DefaultRouter()

router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
