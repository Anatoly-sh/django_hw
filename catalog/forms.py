from django import forms

import catalog
from catalog.models import Product, Version

words_exclude = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user.is_staff is True:
            self.fields['name'].widget.attrs['disabled'] = True
            self.fields['description'].widget.attrs['disabled'] = True
            self.fields['purchase_price'].widget.attrs['disabled'] = True
            self.fields['preview'].widget.attrs['disabled'] = True

        if self.user.has_perm('may_unpublish_product'):
            del self.fields['published']
        if self.user.has_perm('can_change_description_product'):
            del self.fields['description']
        if self.user.has_perm('can_change_category_product'):
            del self.fields['category']

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
