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

    # email = models.EmailField(
    #     verbose_name="Email",
    # )

   

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.name

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'investment'
        verbose_name = 'investor'
        verbose_name_plural = 'investor'
