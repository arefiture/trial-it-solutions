from django.db import models

from fin_pull.exceptions import FixedRelationError


class AbstractFk(models.ForeignKey):
    """
    Явно указываю, что это лишь шаблон для будущих полей.

    Обязательно передавайте to='app.<ModelName>' при вызове `__init__`
    Также переопределить correct_to у родителей
    """
    description = 'Абстрактное поле для логики FK'
    correct_to: str

    def __init__(self, *args, **kwargs):
        to: str = kwargs.get('to', '')
        if to.lower() != self.correct_to.lower():
            raise FixedRelationError(self.__class__)

        kwargs.setdefault('on_delete', models.PROTECT)
        super().__init__(*args, **kwargs)


class CategoryFK(AbstractFk):
    description = 'FK Category'
    correct_to = 'fin_pull.Category'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', 'Категория')
        kwargs.setdefault('to', self.correct_to)
        super().__init__(*args, **kwargs)


class SubCategoryFK(AbstractFk):
    description = 'FK SubCategory'
    correct_to = 'fin_pull.SubCategory'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', 'Подкатегория')
        kwargs.setdefault('to', self.correct_to)
        super().__init__(*args, **kwargs)


class StatusFK(AbstractFk):
    description = 'FK Status'
    correct_to = 'fin_pull.Status'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', 'Статус')
        kwargs.setdefault('to', self.correct_to)
        super().__init__(*args, **kwargs)


class HistoryTypeFK(AbstractFk):
    description = 'FK HistoryType'
    correct_to = 'fin_pull.HistoryType'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', 'Тип')
        kwargs.setdefault('to', self.correct_to)
        super().__init__(*args, **kwargs)
