# Generated by Django 2.1.5 on 2019-02-11 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0003_auto_20190211_1905'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
