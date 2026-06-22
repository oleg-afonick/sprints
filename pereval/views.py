from django.db import DatabaseError

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from pereval.models import Pereval, Coords, User, Level, Image
from pereval.serializers import (
    PerevalSerializer, CoordsSerializer, UserSerializer,
    LevelSerializer, ImageSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalViewSet(ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'post', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(
                    {"status": 400,
                     "message": serializer.errors,
                     "id": None
                     },
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {"status": 200,
                 "message": None,
                 "id": serializer.instance.pk},
                status=status.HTTP_200_OK
            )
        except DatabaseError as e:
            return Response(
                {"status": 500,
                 "message": "Ошибка подключения к базе данных",
                 "id": None
                 },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
