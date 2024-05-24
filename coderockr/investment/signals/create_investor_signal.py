from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Investor
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=Investor)
def send_email_investor(sender, instance, created, **kwargs):
    '''Envia um e-mail de boas-vindas após a criação de um novo Investor.'''
    if created:
        dono = settings.EMAIL_HOST_USER
        recipient = instance.user.email
        subject = 'Seja bem-vindo ao Investment Coderockr'
        html_message = render_to_string('email_investor_create.html', {'instance': instance})
        plain_message = strip_tags(html_message)
        
        email = EmailMultiAlternatives(subject, plain_message, dono, [recipient])
        email.attach_alternative(html_message, "text/html")
        
        try:
            email.send()
        except Exception as e:
            print(f"Falha ao enviar e-mail de boas-vindas: {e}")
