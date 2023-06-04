from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category, BlogRecord


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


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

# -------------------------------------------------------------------


class BlogRecordListView(ListView):
    model = BlogRecord
    queryset = BlogRecord.objects.filter(published=True)


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count = obj.view_count + 1
        obj.save()
        return obj


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'content', 'preview', 'published')
    success_url = reverse_lazy('catalog:blog-record_list')


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'slug', 'content', 'preview', 'published', 'view_count')

    def get_success_url(self):
        return self.object.get_absolute_url()


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('catalog:blog-record_list')


def toggle_activity(request, slug):
    record_item = get_object_or_404(BlogRecord, slug=slug)
    record_item.toggle_published()
    return redirect(reverse('catalog:blog-record_list'))
