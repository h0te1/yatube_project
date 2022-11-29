from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)
