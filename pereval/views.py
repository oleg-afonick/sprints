from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pereval.models import Pereval, User, Coords, Level, Images
from pereval.serializers import PerevalSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PerevalSerializer


class CoordsViewSet(ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = PerevalSerializer

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = PerevalSerializer

class ImagesViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = PerevalSerializer

class PerevalViewSet(ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(
                    {'status': 400, 'message': serializer.errors, 'id': None},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(
                {'status': 200, 'message': None, 'id': serializer.instance.id},
                status=status.HTTP_200_OK
            )
        except DatabaseError:
            return Response(
                {'status': 500, 'message': "Ошибка подключения к базе данных", 'id': None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )