# Generated by Django 4.0.4 on 2022-10-10 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0014_alter_reportstatus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewstatus',
            options={'managed': False, 'verbose_name': 'Список кандидатов', 'verbose_name_plural': 'Список кандидатов'},
        ),
    ]
