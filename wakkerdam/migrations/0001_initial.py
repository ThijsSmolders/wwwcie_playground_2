# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('state', models.CharField(default=b'join', max_length=10, choices=[(b'join', b'Players are joining'), (b'start', b'The game is starting'), (b'day', b'Playing; it is day in the game'), (b'night', b'Playing; it is night in the game'), (b'over', b'The game has been completed!')])),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('role', models.CharField(default=b'civilian', max_length=10, null=True, blank=True, choices=[(b'civilian', b'Ordinary citizen'), (b'werewolf', b'Hungry mothafucka')])),
                ('alive', models.BooleanField(default=True)),
                ('game', models.ForeignKey(related_name=b'players', to='wakkerdam.Game')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('game', 'user')]),
        ),
    ]
