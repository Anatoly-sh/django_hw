from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


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
    return render(request, 'catalog/contacts.html')
