from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    likes = models.IntegerField(default=0, verbose_name='Нравится')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Пост'
        ordering = ['-title', 'author']