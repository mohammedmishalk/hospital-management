# Generated by Django 3.2.9 on 2022-01-17 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospial', '0005_alter_schedule_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='udistrict',
        ),
    ]
