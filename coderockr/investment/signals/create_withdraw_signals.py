from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Withdraw, Investiment
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

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

        dono = settings.EMAIL_HOST_USER
        recipient = instance.investment.owner.user.email
        subject = 'Saque Feito com Sucesso'
        html_message = render_to_string('email_withdraw_create.html', {'instance': instance})
        plain_message = strip_tags(html_message)
        
        email = EmailMultiAlternatives(subject, plain_message, dono, [recipient])
        email.attach_alternative(html_message, "text/html")
        
        try:
            email.send()
        except Exception as e:
            print(f"Falha ao enviar e-mail de boas-vindas: {e}")



