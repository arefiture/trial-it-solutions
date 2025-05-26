"""
Поля, не попавшие в общие наборы
"""

from django.db import models


# Integer fields

class Amount(models.PositiveIntegerField):  # Зачем вынес? А вдруг сумма будет в нескольких местах?
    description = 'Количество рублей или сумма в рублях'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', 0)
        kwargs.setdefault('verbose_name', 'Сумма средств')
        super().__init__(*args, **kwargs)
