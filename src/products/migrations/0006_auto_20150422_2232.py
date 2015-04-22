# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150420_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': 'atrybut', 'verbose_name_plural': 'atrybuty'},
        ),
        migrations.AlterModelOptions(
            name='attributetype',
            options={'verbose_name': 'typ atrybutu', 'verbose_name_plural': 'typy atrybut\xf3w'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'kategoria', 'verbose_name_plural': 'kategorie'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'produkt', 'verbose_name_plural': 'produkty'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'zdj\u0119cie', 'verbose_name_plural': 'zdj\u0119cia'},
        ),
    ]
