# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'C', b'Cart'), (b'O', b'Order'), (b'P', b'Paid Order'), (b'R', b'Realized'), (b'X', b'Cancelled')])),
                ('address', models.TextField()),
                ('product', models.ForeignKey(related_name='orders', to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
