from django.db import models


class Investiment(models.Model):

    owner = models.CharField(
        verbose_name='proprietário',
        max_length=100,
    )

    creation_date = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    value = models.DecimalField(
        verbose_name="Valor",
        max_digits=10,
        decimal_places=2
    )
    

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.owner

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'Investment'
        verbose_name_plural = 'Investmentes'
