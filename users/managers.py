from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email: str, first_name: str, last_name: str, phone: str, role: str, password=None):
        """
        Создает пользователя и возвращает объект user
        """
        if not email:
            raise ValueError("Попытка создания пользователя без email")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            phone=phone,
            role=role if role else 'user'
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role, password=None):
        """
        Same as create_user(), but sets is_staff and is_superuser to True.
        """
        if not email:
            raise ValueError("Попытка создания пользователя без email")
        if role != 'admin':
            raise ValueError('Доступно к созданию только пользователи Администраторы!')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            phone=phone,
            role="admin",
            password=password
        )
        #user.is_staff = True
        #user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def has_perm(self):
        pass
