from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter

from pereval.views import PerevalViewSet
from sprints.yasg import urlpatterns as yasg_urls

router = DefaultRouter()

router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', include(router.urls)),
]

urlpatterns += yasg_urls
