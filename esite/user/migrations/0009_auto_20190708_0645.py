# Generated by Django 2.2.3 on 2019-07-08 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190708_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='0726cccf-9731-4c74-b9bb-9d8a7a043e1d', max_length=36, null=True, unique=True, verbose_name='uuid'),
        ),
    ]
