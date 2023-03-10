# Generated by Django 4.0.4 on 2022-05-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0011_alter_control_options_alter_subdivision_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=150, verbose_name='Специальность')),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidateStatus',
            field=models.BooleanField(blank=True, choices=[(True, 'Завершено'), (False, 'В работе')], null=True, verbose_name='Статус кандидата'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='speciality',
            field=models.ForeignKey(blank=True, help_text='Выберите специальность', null=True, on_delete=django.db.models.deletion.PROTECT, to='candidates.speciality', verbose_name='Специальность'),
        ),
    ]
