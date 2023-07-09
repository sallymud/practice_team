from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField('Отчество', max_length=25, default='')
    birthday_date = models.DateField('День рождения', null=True)