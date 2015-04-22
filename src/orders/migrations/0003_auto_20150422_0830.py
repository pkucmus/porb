# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150422_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpossitions',
            old_name='odred',
            new_name='order',
        ),
    ]
