# Generated by Django 3.2.9 on 2021-11-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='sgender',
            field=models.CharField(default='', max_length=50),
        ),
    ]
