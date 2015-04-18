# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150406_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'products/', verbose_name=b'photo'),
        ),
    ]
