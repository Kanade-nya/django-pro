# Generated by Django 5.0.6 on 2024-05-30 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vueapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='character',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='vueapi.character'),
        ),
    ]
