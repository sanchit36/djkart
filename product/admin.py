from django.contrib import admin
from .models import Product, Category, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'is_featured', 'image')
    list_filter = ('date_added', 'is_featured')
    list_editable = ('is_featured', 'image')
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Gerenal Info', {
            'classes': ('wide',),
            'fields': ('title', 'slug', 'price', 'discount_price', 'category', 'tags', 'image'),
        }),
        ('Product Discription', {
            'fields': ('short_description', 'long_description')
        }),
        ('Featured', {'fields': ('is_featured',)}),
        ('Shipping info', {
            'fields': ('weight', 'length', 'breath', 'height')
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
