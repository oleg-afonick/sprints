from django.db import models

"""
{
  "beauty_title": "пер.",
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

    "coords":{
  "latitude": 45.3842,
  "longitude": 7.1525,
  "height": 1200},

  "level": {"winter": "",
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},

   "images": [{"data": "картинка1", "title": "Седловина"}, {"data": "картинка2", "title": "Подъём"}]
}

"""


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    winter = models.CharField(max_length=255, null=True, blank=True)
    summer = models.CharField(max_length=255, null=True, blank=True)
    autumn = models.CharField(max_length=255, null=True, blank=True)
    spring = models.CharField(max_length=255, null=True, blank=True)


class Pereval(models.Model):
    STATUS = (
        ('new', 'новый'), ('pending', 'в работе'),
        ('accepted', 'принят'), ('rejected', 'отклонён')
    )
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255, null=True, blank=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS, default='new')


class Images(models.Model):
    data = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
