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
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('address_line', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderPossition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.DecimalField(max_digits=13, decimal_places=2)),
                ('unit_type', models.CharField(max_length=3, choices=[(b'kg', b'kg'), (b'pcs', b'pcs')])),
                ('order', models.ForeignKey(related_name='possitions', to='orders.Order')),
                ('product', models.ForeignKey(related_name='orders', to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
