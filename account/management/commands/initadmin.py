from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = "Initialize admin"

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).count() == 0:
            admin = User.objects.create_superuser(
                email=settings.ADMIN_EMAIL,
                username=settings.ADMIN_USERNAME,
                password=settings.ADMIN_PASSWORD
            )
            admin.is_active = True
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
