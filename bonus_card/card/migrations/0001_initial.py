# Generated by Django 3.2.16 on 2022-12-04 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_use', models.DateTimeField(auto_now_add=True, verbose_name='date of use')),
                ('amount', models.PositiveIntegerField(verbose_name='purchase amount')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField(verbose_name='series number for card')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='card number')),
                ('release_date', models.DateTimeField(auto_now_add=True, verbose_name='card release date')),
                ('end_date', models.DateTimeField(verbose_name='end date of card activity')),
                ('card_status', models.CharField(choices=[('activated', 'activated'), ('not activated', 'activated'), ('overdue', 'overdue')], default='not activated', max_length=13)),
                ('appling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card.appling', verbose_name='card usage')),
            ],
        ),
    ]
