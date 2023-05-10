from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_data.json')   # см. https://django.fun/ru/docs/django/4.1/ref/django-admin/
