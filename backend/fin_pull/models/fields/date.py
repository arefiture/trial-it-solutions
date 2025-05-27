"""
Только поля, связанные с датами.
Пример:
- Дата создания
- Дата обновления
- Дата исключения
"""

from django.db import models
from django.utils.timezone import now


class CreatedDate(models.DateTimeField):
    description = 'Дата создания'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', now)
        kwargs.setdefault('verbose_name', 'Дата создания записи')
        super().__init__(*args, **kwargs)
