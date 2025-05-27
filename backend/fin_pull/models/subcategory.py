from fin_pull.models.abstract import ShortBaseModels
from fin_pull.models.fields import CategoryFK


class SubCategory(ShortBaseModels):
    """Подкатегории ДДС."""

    category = CategoryFK()

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
