# Generated by Django 3.1.4 on 2021-01-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_order_buying_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип заказа'),
        ),
    ]
