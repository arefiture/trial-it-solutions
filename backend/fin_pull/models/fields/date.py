"""
Только поля, связанные с датами.
Пример:
- Дата создания
- Дата обновления
- Дата исключения
"""

from django.db import models


class CreatedDate(models.DateField):
    description = 'Дата создания'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_now_add', True)
        kwargs.setdefault('verbose_name', 'Дата создания записи')
        super().__init__(*args, **kwargs)
