from pprint import pprint

from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.


def index(request):
    """
    Отображение домашней страницы
    """
    # Формирование параметров каталога из БД
    num_categories = Category.objects.all().count()
    num_products = Product.objects.all().count()
    context = {'num_categories': num_categories,
               'num_products': num_products,
               'title': 'Главная'
               }

    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста
    return render(request, 'catalog/index.html', context)


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        full_name = request.POST.get('full_name')
        print(f'Зарегистрирован пользователь {full_name} \n'
              f'с именем: {name}, \n'
              f'электронная почта: {email}, \n'
              f'телефон: {phone}\n')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def card(request):
    context = {
        'category_list': Category.objects.all(),
        'object_list': Product.objects.all(),
        'title': 'Список монет'
    }
    return render(request, 'catalog/card.html', context)


def cards(request):
    context = {
        'category_list': Category.objects.all(),
        'object_list': Product.objects.all(),
        'title': 'Список монет'
    }
    return render(request, 'catalog/products_rew.html', context)


def coin(request, pk):
    coin_item = Product.objects.get(pk=pk)
    context = {
        'object': coin_item,
        'title': coin_item
    }
    return render(request, 'catalog/coin.html', context)

