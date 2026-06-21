from rest_framework import serializers

from pereval.models import Pereval, User, Coords, Level, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
