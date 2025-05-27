from django.db import models

from fin_pull.models.fields import CategoryFK, HistoryTypeFK


class CategoryType(models.Model):
    """Связь категорий и типов."""
    # UDP: В тз явно не указано про 1-M или M-M связь, поэтому использую последнее

    category = CategoryFK()
    history_type = HistoryTypeFK()
    # Для чего поле ниже? Я рассуждаю так: если не устроит M-M связь, можно отключить лишние данные
    # И добиться связи O-M таким образом =)
    # Если совсем напрячься, можно сделать модель(таблицу) для правил. И там сделать настройку,
    # которая бы отвечала за уровень связи этой таблицы. Если останется время - так и сделаю)
    is_active = models.BooleanField(verbose_name='Признак активности записи', default=True)

    class Meta:
        verbose_name = 'связь категории и типа'
        verbose_name_plural = 'связи категорий и типов'
