# Generated by Django 2.2.3 on 2019-07-31 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
