from django.db import models
from django.conf import settings

class Timer(models.Model):

	TYPE_CHOICES = (
		(0, 'Pomodoro'),
		(1, 'ShortBreak'),
		(2, 'LongBreak'),
	)

	type = models.IntegerField('Tipo', choices=TYPE_CHOICES)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='Timer'
	)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)