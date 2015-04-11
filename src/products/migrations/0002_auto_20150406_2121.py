# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/products/', verbose_name=b'photo')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(related_name='images', to='products.Product'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_type',
            field=models.ForeignKey(to='products.AttributeType'),
        ),
        migrations.AddField(
            model_name='product',
            name='attribute',
            field=models.ManyToManyField(related_name='attributes', to='products.Attribute'),
        ),
    ]
