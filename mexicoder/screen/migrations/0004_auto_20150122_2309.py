# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0003_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='team',
            field=models.OneToOneField(to='screen.Team'),
            preserve_default=True,
        ),
    ]
