from django.contrib import admin
from .models import Post

@admin.register(Post) # <- Регистрация модели Post в панели администрирования
class PostAdmin(admin.ModelAdmin):
  # изменяем отображения модели:
  list_display = ['title', 'slug', 'author', 'publish', 'status']
  list_filter = ['status', 'created', 'publish', 'author']
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ['author']
  date_hierarchy = 'publish'
  ordering = ['status', 'publish']