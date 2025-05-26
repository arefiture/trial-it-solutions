from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Загружает фикстуры в правильном порядке"

    def handle(self, *args, **kwargs):
        BONUSES_FIXTURES_PATH = 'fin_pull/fixtures'
        fixture_order = [
            {
                'dir': BONUSES_FIXTURES_PATH,
                'file': 'status.json'
            },
            {
                'dir': BONUSES_FIXTURES_PATH,
                'file': 'history_type.json'
            },
            {
                'dir': BONUSES_FIXTURES_PATH,
                'file': 'category.json',
            },
            {
                'dir': BONUSES_FIXTURES_PATH,
                'file': 'category_type.json'
            },
            {
                'dir': BONUSES_FIXTURES_PATH,
                'file': 'subcategory.json'
            }
        ]

        for fixture in fixture_order:
            dir = fixture['dir']
            file = fixture['file']
            self.stdout.write(self.style.SUCCESS(f'Загружаю {file}...'))
            call_command('loaddata', f'{dir}/{file}')

        self.stdout.write(self.style.SUCCESS("✅ Фикстуры успешно загружены!"))
