from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from main.models import Car, Detail
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(_("User name"), max_length = 255, unique = True)
    avatar = models.ImageField(_("User avatar"), blank = True, default = "default_avatar.png",)
    money = models.PositiveBigIntegerField("Money", blank = True, default = 1000) 
    cars = models.ManyToManyField(Car, blank = True, null = True)
    details = models.ManyToManyField(Detail, blank = True, null = True)

    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_created=True, default=timezone.now)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_query_name='customuser',  
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_query_name='customuser',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["is_active"]

    objects = CustomUserManager()
    
    def update_last_login(self, user):
        user.date_created = timezone.now()
        user.save(update_fields=['date_created'])

    def __str__(self):
        return f"id - {self.id} | {self.username}"