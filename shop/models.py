from django.db import models

class Prods(models.Model):
    name_prod = models.CharField('Назва товару', max_length=20)
    text_prod = models.TextField('Опис Товару')
    date = models.DateField('Дата публікації')
    prod_img = models.FileField('Фото продукта')
    county = models.CharField('Країна виробник', max_length=20)
    brand = models.CharField('Бренд', max_length=20)
    price_prod = models.FloatField('Ціна товару')

    def __str__(self):
        return self.name_prod
