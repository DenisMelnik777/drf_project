# Generated by Django 4.2.4 on 2023-09-09 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0003_lesson_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель курса'),
        ),
    ]