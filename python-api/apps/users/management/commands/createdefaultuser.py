from apps.users.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            name = 'Admin'
            lastname = 'User'
            email = 'admin@admin.com'
            password = 'admin'
            print('Creating account for %s (%s)' % (name, email))
            admin = User.objects.create_superuser(email=email, name=name, lastname=lastname, password=password)
            #admin.is_admin = True
            #admin.save()
        else:
            print('Admin account can only be created if no default admin user exist')