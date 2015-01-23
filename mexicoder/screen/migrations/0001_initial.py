# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('flag', models.ImageField(upload_to=b'countryImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('badge', models.ImageField(upload_to=b'leagueImages')),
                ('creationDate', models.DateTimeField(verbose_name=b'creation date')),
                ('country', models.ForeignKey(to='screen.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dateBirth', models.DateTimeField(verbose_name=b'date of birth')),
                ('height', models.FloatField(default=0.0)),
                ('weight', models.FloatField(default=0.0)),
                ('imageProfile', models.ImageField(upload_to=b'profileImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='screen.Person')),
                ('victories', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('directingPoints', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('screen.person',),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='screen.Person')),
                ('shootingPoints', models.IntegerField(default=0)),
                ('passingPoints', models.IntegerField(default=0)),
                ('dribblingPoints', models.IntegerField(default=0)),
                ('defendingPoints', models.IntegerField(default=0)),
                ('headingPoints', models.IntegerField(default=0)),
                ('foot', models.CharField(default=b'R', max_length=1, choices=[(b'R', b'Right'), (b'L', b'Left')])),
            ],
            options={
            },
            bases=('screen.person',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('badge', models.ImageField(upload_to=b'teamImages')),
                ('creationDate', models.DateTimeField(verbose_name=b'creation date')),
                ('atackPoints', models.IntegerField(default=0)),
                ('defensePoints', models.IntegerField(default=0)),
                ('country', models.ForeignKey(to='screen.Country')),
                ('league', models.ForeignKey(to='screen.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='screen.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.ForeignKey(to='screen.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(to='screen.Team'),
            preserve_default=True,
        ),
    ]
