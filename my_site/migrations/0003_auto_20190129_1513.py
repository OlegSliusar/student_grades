# Generated by Django 2.1.5 on 2019-01-29 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_auto_20190128_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('surname', models.CharField(default=None, max_length=60)),
                ('fRole', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_site.Role')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RemoveField(
            model_name='expertreview',
            name='fAnswer',
        ),
        migrations.RemoveField(
            model_name='expertreview',
            name='fGrade',
        ),
        migrations.DeleteModel(
            name='ExpertReview',
        ),
    ]
