from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from pereval.models import Pereval, User, Coords, Level, Images


class UserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Images
        fields = ['title', 'data']


class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Pereval
        fields = [
            'beauty_title', 'title', 'other_titles', 'connect',
            'add_time', 'user', 'coords', 'level', 'status', 'images'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        user, _ = User.objects.get_or_create(**user_data)
        coords = Coords.objects.create(**coords_data)
        level = Level.objects.create(**level_data)

        pereval = Pereval.objects.create(user=user, coords=coords, level=level, **validated_data)

        for image in images_data:
            Images.objects.create(pereval=pereval, **image)

        return pereval
