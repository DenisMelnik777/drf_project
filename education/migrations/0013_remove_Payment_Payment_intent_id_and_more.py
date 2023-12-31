# Generated by Django 4.2.4 on 2023-09-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_alter_payment_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_intent_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_method_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'cash'), ('transfer', 'transfer')], default='transfer', max_length=100, null=True, verbose_name='Способ оплаты'),
        ),
    ]