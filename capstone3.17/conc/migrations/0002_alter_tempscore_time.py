# Generated by Django 4.0 on 2022-03-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempscore',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]