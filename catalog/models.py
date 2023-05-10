from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=2000, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', max_length=100, verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    purchase_price = models.IntegerField(verbose_name='Стоимость')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} / {self.purchase_price} : {self.category}'

    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'изделия'
        ordering = ('name',)

