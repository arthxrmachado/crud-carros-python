# Generated by Django 4.2.2 on 2023-06-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('cor', models.CharField(max_length=15)),
            ],
        ),
    ]
