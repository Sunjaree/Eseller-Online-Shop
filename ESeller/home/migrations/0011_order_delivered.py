# Generated by Django 3.2.8 on 2022-08-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
