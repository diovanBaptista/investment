from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from ..models import Investiment


@receiver(post_save, sender=Investiment)
def investment_post_save(sender, instance, created, **kwargs):
    '''Realiza ações após a model Investimentation ser salva.'''
    if created:
        value = instance.value 
        date = instance.creation_date
        current_date = datetime.now() 
        date = f"{date}"
        date = datetime.strptime(date, "%Y-%m-%d")

        months_passed = (current_date.year - date.year) * 12 + current_date.month - date.month
        
        # Se o dia atual for menor que o dia de criação, ajusta o número de meses
        if current_date.day < date.day:
            months_passed -= 1

        # Calcula o saldo acumulado multiplicando pelo fator mensal 0,52
        saldo = float(value)
        for _ in range(months_passed):
            saldo += saldo * 0.52

        instance.balance = round(saldo,2)
        instance.save()
