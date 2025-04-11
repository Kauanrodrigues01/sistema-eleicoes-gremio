from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config


class Command(BaseCommand):
    help = 'Creates users'

    def handle(self, *args, **kwargs):
        username = config('ADMIN_USERNAME', default='admin')
        password = config('ADMIN_PASSWORD', default='admin')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        else:
            self.stdout.write(self.style.WARNING('User already exists'))
