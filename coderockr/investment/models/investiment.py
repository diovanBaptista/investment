from django.db import models
from datetime import datetime


class Investiment(models.Model):

    owner = models.CharField(
        verbose_name='proprietário',
        max_length=100,
    )

    creation_date = models.DateField(
        verbose_name='Data de criação',
        # auto_now_add=True
    )

    value = models.DecimalField(
        verbose_name="Valor",
        max_digits=10,
        decimal_places=2
    )


    investment_withdrawal = models.BooleanField(
        verbose_name='Saque do investimento',
        default=False,
    )

    # investment_balance = models.DecimalField(
    #     verbose_name="Saldo do Investimento",
    #     max_digits=10,
    #     decimal_places=2,
    #     default=0
    # )

    @property
    def saldo(self):
        value = self.value 
        date = self.creation_date
        current_date = datetime.now() 

        months_passed = (current_date.year - date.year) * 12 + current_date.month - date.month
        
        # Se o dia atual for menor que o dia de criação, ajusta o número de meses
        if current_date.day < date.day:
            months_passed -= 1

        # Calcula o saldo acumulado multiplicando pelo fator mensal 0,52
        saldo = float(value)
        for _ in range(months_passed):
            saldo += saldo * 0.52

        return round(saldo,2)

        

    

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.owner} - {self.saldo}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'Investment'
        verbose_name_plural = 'Investmentes'
