from django.db import models
from .. models import Investiment
from datetime import datetime

class Withdraw(models.Model):

    investment = models.ForeignKey(
        Investiment,
        verbose_name='Investmento',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    value = models.DecimalField(
        verbose_name="Valor",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    ) 

    withdrawal_date = models.DateField(
        verbose_name='Data do Saque',
        # auto_now_add=True
    )

    withdraw_full_amount = models.BooleanField(
        verbose_name='Saquar Valor total',
        default=False,
    )

    @property
    def imposto(self):
        saldo = self.investment.saldo
        valor = saldo - float(self.investment.value)
        create_investment = f"{self.investment.creation_date}"
        withdrawal_date = f"{self.withdrawal_date}"
        create_investment = datetime.strptime(create_investment, "%Y-%m-%d")
        withdrawal_date = datetime.strptime(withdrawal_date, "%Y-%m-%d")
        diff_years = (withdrawal_date - create_investment).days / 365

        if diff_years < 1:
            percentual_imposto = 0.225  
        elif 1 <= diff_years < 2:
            percentual_imposto = 0.185  
        else:
            percentual_imposto = 0.15 

        imposto = valor * percentual_imposto
        return round(imposto, 2)
    
    @property
    def valor_final(self):
        return round(self.investment.saldo - self.imposto, 2)




    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"Saque do investimento {self.investment}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'withdraw'
        verbose_name_plural = 'withdraw'
