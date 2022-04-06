from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)
from django_countries.fields import CountryField

class CustomUser(AbstractUser):

    """ custom user model """
    vendor_choice=[
        ('Enabled','Enabled'),
        ('Disabled','Disabled'),
    ]

    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.BigIntegerField(unique=True)
    country = CountryField()
    Pincode=models.PositiveSmallIntegerField(null=True)
    profile=models.ImageField(upload_to='profile/')

    # usermembershipplan=models.CharField(max_length=200)
    # vendorstaus=models.CharField(max_length=20,choices=vendor_choice)

    #     username
    #     password
    #     repeatpassword
    #     underaffilite---user list
    #     underlevel----level1,level2,level3
    #     country---countries list
    #     groups

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile','Pincode']


    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def create_user(self):
        pass

    class Meta:
        verbose_name = 'User'
        ordering = ['-date_joined']
        