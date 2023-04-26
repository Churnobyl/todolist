# Generated by Django 4.2 on 2023-04-26 11:03

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=articles.models.rename_imagefile_to_uuid),
        ),
    ]
