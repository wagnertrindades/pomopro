from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User Custom with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User
    """

    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100)
    date_birth = models.DateField('Data de Nascimento', null=True, blank=True)
    image = models.ImageField(
        upload_to="core/images", verbose_name='Imagem', null=True, blank=True
    )
    is_staff = models.BooleanField('É administrador?', blank=True, default=False)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    def get_short_name(self):
        return str(self)

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name='Usuário'
        verbose_name_plural='Usuários'

class PasswordReset(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return "{0} em {1}".format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']