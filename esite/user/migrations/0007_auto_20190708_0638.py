# Generated by Django 2.2.3 on 2019-07-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190708_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='3b25cb85-7927-4267-95e9-72a002e89769', max_length=36, null=True, unique=True, verbose_name='uuid'),
        ),
    ]
