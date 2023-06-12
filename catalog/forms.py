from django import forms

from catalog.models import Product

words_exclude = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

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
