# Generated by Django 2.1.5 on 2019-01-31 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0012_auto_20190131_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='fSection',
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
    ]
