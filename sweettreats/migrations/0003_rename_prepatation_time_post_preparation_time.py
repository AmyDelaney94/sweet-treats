# Generated by Django 3.2.13 on 2022-06-22 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweettreats', '0002_auto_20220622_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='prepatation_time',
            new_name='preparation_time',
        ),
    ]