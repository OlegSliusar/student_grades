# Generated by Django 2.1.5 on 2019-01-30 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_user_frole'),
        ('my_site', '0006_auto_20190130_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_like', models.BooleanField()),
                ('fGrade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_site.Grade')),
                ('fQuestion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_site.Question')),
                ('fUser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('fAnswer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='answers.Answer')),
                ('fGrade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_site.Grade')),
                ('fUserExpert', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
