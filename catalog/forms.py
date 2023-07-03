from django import forms

from catalog.models import Product, Version

words_exclude = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('a_user',)       # убираем из формы

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if set(words_exclude) & set(cleaned_data.lower().split()):
            raise forms.ValidationError('Эти товары запрещены')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if set(words_exclude) & set(cleaned_data.lower().split()):
            raise forms.ValidationError('Эти товары запрещены')
        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
