# Generated by Django 2.1.5 on 2019-02-08 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allactions', '0010_auto_20190204_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'ordering': ['id']},
        ),
    ]