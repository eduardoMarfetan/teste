# Generated by Django 5.0.3 on 2024-03-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuapp',
            name='id_ip',
            field=models.IntegerField(),
        ),
    ]
