from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


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

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.pk})


class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogrecord/', max_length=100, verbose_name='Изображение', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def get_absolute_url(self):
        # return reverse('blog-record_detail', args=[str(self.id)])
        return reverse('catalog:blog-record_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_title = translit(self.title, 'ru', reversed=True)
            self.slug = slugify(transliterated_title, allow_unicode=True)
        super().save(*args, **kwargs)

    def toggle_published(self):
        self.published = not self.published
        self.save()


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.CharField(max_length=50, verbose_name='Электронная почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    full_name = models.CharField(max_length=100, verbose_name='Полное имя', **NULLABLE)

    def __str__(self):
        return f'{self.name} / {self.phone}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)


class Version(models.Model):
    name = models.ForeignKey(Product, verbose_name='Наименование', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Имя версии', **NULLABLE)
    version_is_active = models.BooleanField(default=False, verbose_name='Признак версии')

    def __str__(self):
        return f'{self.name} -- версия/{self.version_name} : {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('name',)
