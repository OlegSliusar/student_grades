# Generated by Django 2.1.5 on 2019-02-11 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_auto_20190211_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fUserExpert',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
