import enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(enum.Enum):
    user_role = "user"
    admin_role = "admin"


class User(AbstractBaseUser):
    objects = UserManager()

    ROLES = [("user", UserRoles.user_role.value),
             ("admin", UserRoles.admin_role.value)]

    first_name = models.CharField(max_length=20, blank=False, null=False, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=30, blank=False, null=False, validators=[MinLengthValidator(2)])
    phone = PhoneNumberField(null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.CharField(max_length=5, choices=ROLES, blank=False, null=False)
    image = models.ImageField(upload_to='users_images/')
    is_active = models.BooleanField()

    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]
    USERNAME_FIELD = "email"

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.admin_role.value

    @property
    def is_user(self):
        return self.role == UserRoles.user_role.value

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)
