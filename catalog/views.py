from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, BlogRecord, Contacts, Version


# Create your views here.

class MainListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainListView, self).get_context_data(*args, **kwargs)
        context['category_objects'] = Category.objects.all().count()  # в шаблоне переменная {{ category_objects }}
        return context


# fbv:
# def index(request):
#     """
#     Отображение домашней страницы
#     """
#     # Формирование параметров каталога из БД
#     num_categories = Category.objects.all().count()
#     num_products = Product.objects.all().count()
#     context = {'num_categories': num_categories,
#                'num_products': num_products,
#                'title': 'Главная'
#                }
#
#     # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста
#     return render(request, 'catalog/index.html', context)


class ContactCreateView(CreateView):
    template_name = 'catalog/contacts.html'

    def get(self, request, *args, **kwargs):
        contacts_info = Contacts.objects.all()
        return render(request, self.template_name, {'contacts_info': contacts_info})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        # в БД пока не пишем (выполнить миграцию!)
        # contact = Contacts(name=name, phone=phone, email=email, full_name=full_name)
        # contact.save()
        print(f'Новый контакт: {name} ({phone} / {email} / {full_name})')
        return render(request, 'catalog/contacts.html')  # вернуться в другой шаблон


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         full_name = request.POST.get('full_name')
#         print(f'Зарегистрирован пользователь {full_name} \n'
#               f'с именем: {name}, \n'
#               f'электронная почта: {email}, \n'
#               f'телефон: {phone}\n')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# -------------------------------------------------------------------

'''
Создание продукта с использованием форм
'''


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = None
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        product.a_user = self.request.user
        product.save()
        return super().form_valid(form)


'''
Редактирование продукта с использованием форм
'''


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = None
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form_with_formset.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:product_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


'''
Удаление продукта
'''


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = None
    model = Product
    success_url = reverse_lazy('catalog:product_list')


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
