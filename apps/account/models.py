import email
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, password, email, **extra_fields):
        if not email:
            raise ValueError('email is invalid')
        email= self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email,password, **extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create(email,password, **extra_fields)


class CustomUser(AbstractBaseUser):
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, primary_key=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(6, '0123456789')
        self.activation_code=code
        self.save()
        
        
    def activate_with_code(self, activation_code):
        if self.activation_code != activation_code:
            raise Exception('Invalid activation code')
        self.is_active= True
        self.activation_code = ""
        self.save()
