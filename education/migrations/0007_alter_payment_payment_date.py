# Generated by Django 4.2.4 on 2023-09-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата оплаты'),
        ),
    ]