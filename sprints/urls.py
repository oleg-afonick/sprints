from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from pereval.views import PerevalViewSet

router = routers.DefaultRouter()

router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]