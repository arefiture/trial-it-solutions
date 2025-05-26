from django.db import models

from fin_pull.models.fields import (
    Amount,
    CategoryFK,
    CreatedDate,
    SubCategoryFK,
    StatusFK,
    HistoryTypeFK
)


class History(models.Model):
    """Запись о движении денежных средств."""

    created_at = CreatedDate()
    # Чтоб не пропали ценные данные (деньги же)) ) при удалении статуса - делаю защиту на удаление
    status = StatusFK()
    history_type = HistoryTypeFK()
    category = CategoryFK()
    subcategory = SubCategoryFK()
    # Количеств средств указано в рублях, могу предположить, что ТОЛЬКО в рублях, без копеек.
    # Если же имела в виду сумма с копейками, то в любом случае вместо 15.64 руб можно хранить число
    # 1564, а на уровне отображения устанавливать запятую. Вычисления в некоторых случаях точнее
    amount = Amount()
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'запись о ДДС'
        verbose_name = 'записи о ДДС'
