from fin_pull.models.abstract import ShortBaseModels


class Status(ShortBaseModels):
    """Статус ДДС."""

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'
