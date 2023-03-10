# Generated by Django 4.0.3 on 2022-05-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_product_description_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to=',images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
