from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Юбилейные монеты',
             'description': 'Монеты, посвященные круглым датам'
             },
            {'name': 'Монеты Европы',
             'description': 'Монеты, выпущенные в Европе'
             }
        ]
        product_list = [
            {'name': 'Монета 10 рублей 2003 года',
             'description': 'СПМД «Древние города России — Муром» (Артикул K11-89063)',
             'category': 'Юбилейные монеты',
             'purchase_price': 150
             },
            {'name': 'Монета 10 рублей 2000 года',
             'description': 'ММД «55 лет Великой Победы» (Артикул K11-88397)',
             'category': 'Юбилейные монеты',
             'purchase_price': 50
             },
            {'name': 'Монета 2 евро 2023 года',
             'description': 'Германия «1275 лет со дня рождения Карла Великого» (Артикул M2-62505)',
             'category': 'Монеты Европы',
             'purchase_price': 325
             },
            {'name': 'Монета 10 евро 2002 года',
             'description': 'Испания «XIX зимние Олимпийские Игры 2002 в Солт-Лейк-Сити» (Артикул M2-62501)',
             'category': 'Монеты Европы',
             'purchase_price': 3500
             }
        ]
