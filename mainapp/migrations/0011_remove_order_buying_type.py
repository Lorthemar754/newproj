# Generated by Django 3.1.4 on 2021-01-19 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210119_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buying_type',
        ),
    ]
