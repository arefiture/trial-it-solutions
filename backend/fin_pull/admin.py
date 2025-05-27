from django.contrib import admin

from fin_pull.models.category import Category
from fin_pull.models.category_type import CategoryType
from fin_pull.models.subcategory import SubCategory
from fin_pull.models.history import History
from fin_pull.models.history_type import HistoryType
from fin_pull.models.status import Status


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'history_type')
    list_filter = ('category', 'history_type')
    ordering = ('id',)


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    list_filter = ('category', )
    search_fields = ('name', 'slug',)
    ordering = ('id',)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'status', 'history_type', 'category', 'subcategory', 'amount', 'comment')
    list_editable = ('created_at', 'status', 'history_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('status', 'history_type', 'category', 'subcategory', )


@admin.register(HistoryType)
class HistoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('id',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('id',)
