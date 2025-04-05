import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create an admin user if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        admin_phone = os.getenv("ADMIN_PHONE", "00000000000")
        password = os.getenv("ADMIN_PASS", "admin")

        if not User.objects.filter(phone_number=admin_phone).exists():
            User.objects.create_superuser(
                phone_number=admin_phone,
                password=password,
                first_name='관리자',
                last_name='초기',
                nickname='admin',
                birthday='1111-11-11'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write('Superuser already exists.')
