# Generated by Django 3.1.5 on 2021-02-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzastore', '0005_auto_20210201_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
