# Generated by Django 2.2.3 on 2019-08-02 09:11

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20190725_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniquepage',
            name='about',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]
