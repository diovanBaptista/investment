from django.db import models
from datetime import datetime
from .investor import Investor

class Investiment(models.Model):

    owner = models.ForeignKey(
       Investor,
        verbose_name='proprietário',
        on_delete=models.DO_NOTHING
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

    balance = models.DecimalField(
        verbose_name="Saldo",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    @property
    def saldo(self):
        from .withdraw import Withdraw
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

        # if self.investment_withdrawal:
        #     withdraw = Withdraw.objects.get(id=self.id)
            # saldo = withdraw.valor_final - float(self.value)

        return round(saldo,2)

        

    

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.owner} - {self.saldo}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'Investment'
        verbose_name_plural = 'Investmentes'
