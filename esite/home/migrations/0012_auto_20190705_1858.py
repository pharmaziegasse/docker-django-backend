# Generated by Django 2.2.3 on 2019-07-05 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190705_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='button',
            name='button_class',
        ),
        migrations.RemoveField(
            model_name='button',
            name='button_id',
        ),
    ]