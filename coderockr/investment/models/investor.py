from django.db import models
from django.contrib.auth.models import User

class Investor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=16,
    )

    @property
    def data_criacao(self):
        return self.user.date_joined if self.user else None

   

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'investment'
        verbose_name = 'investor'
        verbose_name_plural = 'investor'
