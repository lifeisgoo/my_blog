from django.contrib import admin
from .models import BlogModel, CategoryModel

@admin.register(CategoryModel)
class CategoryModeladmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id','name']
    search_fields = ['name']



@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'created_at']
    list_display_links = ['tittle', 'created_at']
    list_filter = ['created_at']
    search_fields = ['tittle', 'body']

