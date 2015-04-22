# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150420_2112'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPossitions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='orderpossitions',
            name='odred',
            field=models.ForeignKey(related_name='order_possitions', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='orderpossitions',
            name='product',
            field=models.ForeignKey(related_name='order_possitions', to='products.Product'),
        ),
    ]
