from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField('Отчество', max_length=25, default='')
    birthday_date = models.DateField('День рождения', null=True)
    creator = models.BooleanField('Составитель тестов', default=False)
    teacher = models.BooleanField('Преподаватель', default=False)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Добавьте дополнительные поля профиля, например, роль пользователя
    ROLES = (
        ('test_creator', 'Составитель тестов'),
        ('test_taker', 'Студент'),
        ('test_grader', 'Преподаватель')
    )
    role = models.CharField(max_length=15, choices=ROLES)