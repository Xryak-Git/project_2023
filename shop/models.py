from datetime import datetime
from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField('Title', max_length=20, default='Товарчик')
    price = models.IntegerField('Price', default=0)
    date = models.DateTimeField('Publsih date', auto_now_add=False, blank=True, default=datetime.now())
    image = models.ImageField(upload_to='images', default='images/1.jpeg')

    def __str__(self):
        return f'{self.title} | {self.price} | {self.date}'

    def get_absolute_url(self): # Тут мы создали новый метод
        return f'/shop/{self.id}'
