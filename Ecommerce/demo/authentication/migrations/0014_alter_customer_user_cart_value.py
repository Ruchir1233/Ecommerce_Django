# Generated by Django 4.0.3 on 2022-05-17 10:07

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_customer_user_cart_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_cart_value',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
