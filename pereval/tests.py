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

    def test_create(self):
        url = reverse('pereval-list')
        data = {
            "beauty_title": "перевал 3",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",

            "add_time": "2021-09-22 13:18:13",
            "user": {
                "email": "qwerty@mail.ru",
                "fam": "Пупкин",
                "name": "Василий",
                "otc": "Иванович",
                "phone": "+7 555 55 55"},

            "coords": {
                "latitude": 45.3842,
                "longitude": 7.1525,
                "height": 1200},

            "level": {"winter": "",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": ""},

            "images": [
                {"data": "картинка1", "title": "Седловина"},
                {"data": "картинка2", "title": "Подъём"}
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(3, Pereval.objects.all().count())

    def test_update(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval_2.pk})
        data = {
            "beauty_title": "beauty_title_222"
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, json_data, content_type='application/json')
        self.pereval_2.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.pereval_2.beauty_title, "beauty_title_222")
