# Generated by Django 2.1.5 on 2019-01-31 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allactions', '0002_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='fStep',
        ),
    ]