from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
  class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'

  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  body = models.TextField()
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

  class Meta: # <- используем мета-класс для того, чтобы django сортировал все посты в соответствии с полем publish. 
    ordering = ['-publish'] # <- ставим дефис перед именем поля, для того чтобы порядок был убывающим.
    indexes = [
      models.Index(fields=['-publish']),
    ]

  def __str__(self): # <- метод, возвращающий строковый литерал с удобным для чтения представлением объекта, к примеру в панели аднимистрирования посты будут называться как их заголовки.
    return self.title