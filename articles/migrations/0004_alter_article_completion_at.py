# Generated by Django 4.2 on 2023-04-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_user_id_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='completion_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='완료시간'),
        ),
    ]
