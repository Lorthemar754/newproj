# Generated by Django 3.1.4 on 2020-12-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201214_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
