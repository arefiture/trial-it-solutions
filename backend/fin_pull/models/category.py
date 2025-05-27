from django.db import models

from fin_pull.models.abstract import ShortBaseModels


class Category(ShortBaseModels):
    """Категории ДДС."""
    history_type = models.ManyToManyField(
        to='fin_pull.HistoryType',
        through='CategoryType',
        related_name='categories'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
