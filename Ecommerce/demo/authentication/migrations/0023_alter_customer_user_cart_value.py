# Generated by Django 4.0.3 on 2022-07-15 15:39

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_alter_customer_user_cart_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_cart_value',
            field=picklefield.fields.PickledObjectField(default=0, editable=False),
        ),
    ]
