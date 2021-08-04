# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20210726_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrye',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(to='learning_logs.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
