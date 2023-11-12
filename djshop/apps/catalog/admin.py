from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from djshop.apps.catalog.models import Category


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, CategoryAdmin)
