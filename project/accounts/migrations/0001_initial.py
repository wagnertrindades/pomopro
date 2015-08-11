# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import project.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail', unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('date_birth', models.DateField(blank=True, verbose_name='Data de Nascimento', null=True)),
                ('image', models.ImageField(upload_to='core/images', verbose_name='Imagem', null=True, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('groups', models.ManyToManyField(related_query_name='user', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', project.accounts.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('key', models.CharField(max_length=100, verbose_name='Chave', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets')),
            ],
            options={
                'verbose_name_plural': 'Novas Senhas',
                'ordering': ['-created_at'],
                'verbose_name': 'Nova Senha',
            },
        ),
    ]
