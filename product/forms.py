from django import forms
from django.utils.text import slugify
from .models import Product, Category, Tag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('date_added', 'slug')

    def save(self, commit=True):
        p = super(ProductForm, self).save(commit=False)
        p.slug = slugify(self.cleaned_data['title'])
        if commit:
            p.save()
        return p


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("name",)

    def save(self, commit=True):
        p = super(CategoryForm, self).save(commit=False)
        p.slug = slugify(self.cleaned_data['name'])
        if commit:
            p.save()
        return p


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ("name",)
