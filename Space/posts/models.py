from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст записи',
        help_text='Введите текст записи',
    )
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор записи',
    )

    def __str__(self) -> str:
        return str(self.text[:15])

    class Meta:
        ordering = ['-created']
