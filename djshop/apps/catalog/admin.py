from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from djshop.apps.catalog.models import Category, ProductClass, Option, ProductAttribute


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Option)


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 2


class AttributeCountFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attr_count'


    def lookups(self, request, model_admin):
        return [
            ('more_2', 'More Than 2'),
            ('less_2', 'Less Than 2'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'more_2':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__gt=2) 
        if self.value() == 'less_2':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__lt=2)



@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'require_shipping', 'track_stock', 'attribute_count')
    list_filter = ('require_shipping', 'track_stock', AttributeCountFilter)
    inlines = [ProductAttributeInline]
    actions = ['enable_track_stock']
    prepopulated_fields = {'slug' : ('title',)}


    def attribute_count(self, obj):
        return obj.attributes.count()
    

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)



admin.site.register(Category, CategoryAdmin)
