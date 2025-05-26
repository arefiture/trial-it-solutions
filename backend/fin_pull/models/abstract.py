from django.db import models
from slugify import slugify

from fin_pull.constants import LONG_SLUG_LENGTH


class ShortBaseModels(models.Model):
    """
    Абстрактная модель. Содержит поля:
    - id
    - name
    - slug
    """

    name = models.CharField(
        verbose_name='Наименование',
        max_length=LONG_SLUG_LENGTH,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=LONG_SLUG_LENGTH,
        unique=True,
        blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while self.__class__.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
