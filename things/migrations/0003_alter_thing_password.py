# Generated by Django 3.2.16 on 2022-10-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_auto_20221014_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='password',
            field=models.TextField(blank=True),
        ),
    ]
