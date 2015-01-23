# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='creationDate',
            field=models.DateField(verbose_name=b'creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='dateBirth',
            field=models.DateField(verbose_name=b'date of birth'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='creationDate',
            field=models.DateField(verbose_name=b'creation date'),
            preserve_default=True,
        ),
    ]
