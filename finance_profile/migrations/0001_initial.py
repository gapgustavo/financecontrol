# Generated by Django 4.2.3 on 2023-07-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bank', models.CharField(choices=[('NU', 'Nubank'), ('BB', 'Banco do Brasil')], max_length=2)),
                ('wallet_type', models.CharField(choices=[('P', 'Personal'), ('C', 'Company')], max_length=2)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=50)),
                ('essential', models.BooleanField(default=False)),
                ('planning_value', models.FloatField(default=0)),
            ],
        ),
    ]
