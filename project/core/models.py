from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100)
    date_birth = models.DateField('Data de Nascimento', null=True, blank=True)
    image = models.ImageField(
        upload_to="core/images", verbose_name='Imagem', null=True, blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Usuário'
        verbose_name_plural='Usuários'

