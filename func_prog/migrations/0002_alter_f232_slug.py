# Generated by Django 4.1.5 on 2023-08-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func_prog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f232',
            name='slug',
            field=models.SlugField(null=True, verbose_name='URL'),
        ),
    ]
