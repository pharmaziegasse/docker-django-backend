# Generated by Django 2.2.3 on 2019-07-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190707_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='505ccd56-0a03-47ae-9d36-42a824d09e9a', max_length=36, null=True, unique=True, verbose_name='uuid'),
        ),
    ]