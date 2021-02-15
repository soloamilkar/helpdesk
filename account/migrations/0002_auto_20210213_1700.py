# Generated by Django 3.1.6 on 2021-02-13 17:00

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default=account.models.default_image_url, upload_to=account.models.account_image_url),
        ),
    ]