import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pereval.models import Pereval, User, Coords, Level, Images
from pereval.serializers import PerevalSerializer


class PerevalTest(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='beauty_title_1',
            title='title_1',
            other_titles='other_titles_1',
            connect='',
            add_time='2021-09-22T13:18:13Z',
            user=User.objects.create(
                email='email_1@email.com',
                fam='fam_1',
                name='name_1',
                otc='otc_1',
                phone='89000000001',
            ),
            coords=Coords.objects.create(
                latitude=123.00,
                longitude=456.00,
                height=789
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1B',
                autumn='2B',
                spring='',
            )
        )

        self.image_1_1 = Images.objects.create(
            data='data_1_1',
            title='title_1_1',
            pereval=self.pereval_1,
        )
        self.image_1_2 = Images.objects.create(
            data='data_1_2',
            title='title_1_2',
            pereval=self.pereval_1,
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='beauty_title_2',
            title='title_2',
            other_titles='other_titles_2',
            connect='',
            add_time='2021-09-22T13:18:13Z',
            user=User.objects.create(
                email='email_2@email.com',
                fam='fam_2',
                name='name_2',
                otc='otc_2',
                phone='89000000002',
            ),
            coords=Coords.objects.create(
                latitude=123.02,
                longitude=456.02,
                height=792
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1B',
                autumn='',
                spring='2B',
            )
        )

        self.image_2_1 = Images.objects.create(
            data='data_2_1',
            title='title_2_1',
            pereval=self.pereval_2,
        )
        self.image_2_2 = Images.objects.create(
            data='data_2_2',
            title='title_2_2',
            pereval=self.pereval_2,
        )

    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(2, len(serializer_data))

    def test_get_detail(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval_1.pk})
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.data.get('beauty_title'), serializer_data.get('beauty_title'))


