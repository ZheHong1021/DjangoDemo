from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
import uuid

GENDER_CHOICES = [
    ('male', '男性'),
    ('female', '女性'),
    ('other', '其他'),
    ('private', '不公開'),
]

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # UUID當主鍵
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    firstname = models.CharField("名字", max_length=10, blank=True, null=True)
    lastname = models.CharField("姓氏", max_length=10, blank=True, null=True)
    phone_number = models.CharField("手機號碼", max_length=10, blank=True, null=True)
    age = models.IntegerField("年齡", blank=True, null=True)
    gender = models.CharField("性別", max_length=10, choices=GENDER_CHOICES, blank=True, default='private')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"