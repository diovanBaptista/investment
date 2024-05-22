from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Withdraw, Investiment


@receiver(post_save, sender=Withdraw)
def withdraw_post_save(sender, instance, created, **kwargs):
    '''Realiza ações após a model Withdraw ser salva.'''
    if created:
        instance.value = instance.investment.saldo
        instance.save()

        investment = Investiment.objects.get(id=instance.investment.id)

        saldo = instance.valor_final - float(investment.value)

        investment.investment_withdrawal = True
        investment.balance = saldo
        investment.save()


