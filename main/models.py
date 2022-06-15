from operator import mod
from django.db import models

# Create your models here.

class Contacts(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField()
    message = models.TextField('Сообщение')
    sent_at = models.DateTimeField('Время отправки', auto_now_add=True)



class Product(models.Model):
    name = models.CharField("Название товара",max_length=255)
    description = models.CharField("Описание",max_length=255, default='', blank=True, null=True)
    price = models.IntegerField("Цена",default=0)
    image = models.ImageField("Изображение", upload_to='upload/products')
    ingredients = models.TextField('Состав')
    code_product = models.IntegerField('Код товара')
    manufacturer = models.CharField('Производитель', max_length=255)
    country = models.CharField('Страна', max_length=255)
    weight_volume = models.CharField('Вес/Объем', max_length=255)
    age_limit = models.CharField('Минимальный возраст от', max_length=255)
    temperature = models.CharField('Допустимая температура хранения', max_length=255)
    expiration_date = models.CharField('Срок годности', max_length=255)
    date_manufacture = models.DateField('Дата изготовления')
   
class Billing_detail(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    number = models.CharField('Номер телефона', max_length=50)
    email = models.EmailField('Почта')
    country = models.CharField('Страна', max_length=255)
    city = models.CharField('Город', max_length=255)
    street = models.CharField('Улица', max_length=255)
    posta_zip = models.CharField('Почта/Почтовый индекс', max_length=255)
    note_message = models.TextField('Сообщение', null=True, blank=True, default='')
    sent_at = models.DateTimeField('Время отправки', auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class Order(models.Model):
    product = models.CharField('Лекарство', max_length=255)
    p_count = models.IntegerField('Количество')
    p_price = models.IntegerField('Цена')
    p_total = models.IntegerField('Итого')
    customer = models.ForeignKey(Billing_detail,  on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Заказчик")
        


class Feedback(models.Model):
    image = models.ImageField("Изображение", upload_to='upload/reviews')
    review = models.TextField('Сообщение', null=True, blank=True, default='')
    firstLastName = models.CharField('Имя и фамилия', max_length=255)


    



