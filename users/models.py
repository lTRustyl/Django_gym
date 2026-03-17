from django.db import models

class Users(models.Model):
    name_surname = models.CharField('Імя та прізвище', max_length=80)
    login = models.CharField('Логін Користувача', max_length=50)
    password = models.CharField('Пароль користувача',max_length=50)
    passport_id = models.CharField('Дані Паспорта', max_length=6)
    gum_status = models.BooleanField('У залі', default= False)
    discount = models.BooleanField('Знижка', default= False)

    def __str__(self):
        return self.name_surname

