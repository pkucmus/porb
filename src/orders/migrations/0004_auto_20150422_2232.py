# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150422_0830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'zam\xf3wienie', 'verbose_name_plural': 'zam\xf3wienia'},
        ),
        migrations.AlterModelOptions(
            name='orderpossitions',
            options={'verbose_name': 'pozycja', 'verbose_name_plural': 'pozycje'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='post_code',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
