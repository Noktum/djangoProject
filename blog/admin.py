from django.contrib import admin
from .models import Post, Category


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['category']


admin.site.register(Category)  # Регистрация модели нашего поста
admin.site.register(Post)

