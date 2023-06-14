from django.contrib import admin

from catalog.models import Product, Category, BlogRecord, Version


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'version_number', 'version_name', 'version_is_active',)
    list_filter = ('name',)


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'published')
    prepopulated_fields = {'slug': ('title',)}

