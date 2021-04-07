from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def create_user(self, email, name, lastname, password=None):
        if not email:
            raise ValueError('The email is mandatory.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            lastname=lastname
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, name, lastname, password):
        user = self.create_user(email, name, lastname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'lastname']

    def __str__(self):
        return f"{self.name} {self.lastname}"

