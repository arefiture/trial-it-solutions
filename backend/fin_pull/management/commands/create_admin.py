from environs import Env

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

env = Env()
env.read_env()


class Command(BaseCommand):
    help = 'Создаёт суперпользователя из переменных окружения'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = env.str('DJANGO_SUPERUSER_USERNAME')
        email = env.str('DJANGO_SUPERUSER_EMAIL')
        password = env.str('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Суперпользователь "{username}" создан.'))
        else:
            self.stdout.write(self.style.WARNING(f'Суперпользователь "{username}" уже существует.'))
