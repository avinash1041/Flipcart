# Generated by Django 3.2.3 on 2021-05-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.CharField(max_length=200),
        ),
    ]
