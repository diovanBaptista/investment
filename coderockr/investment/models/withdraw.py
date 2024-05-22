from django.db import models
from .. models import Investiment

class Withdraw(models.Model):

    investment = models.ForeignKey(
        Investiment,
        verbose_name='Investmento',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False
    )

    value = models.DecimalField(
        verbose_name="Valor",
        max_digits=10,
        decimal_places=2
    ) 

    withdrawal_date = models.DateField(
        verbose_name='Data do Saque',
        # auto_now_add=True
    )

    withdraw_full_amount = models.BooleanField(
        verbose_name='Saquar Valor total',
        default=False,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"Saque do investimento {self.investment}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'withdraw'
        verbose_name_plural = 'withdraw'
