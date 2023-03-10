# Generated by Django 4.0.3 on 2022-05-17 10:43

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_remove_customer_users_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_cart_value',
            field=picklefield.fields.PickledObjectField(default=0, editable=False),
            preserve_default=False,
        ),
    ]