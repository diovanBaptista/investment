# Generated by Django 3.2.12 on 2024-05-22 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0005_withdraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='withdraw_full_amount',
            field=models.BooleanField(default=False, verbose_name='Saquar Valor total'),
        ),
    ]