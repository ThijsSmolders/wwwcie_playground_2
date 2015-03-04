# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wakkerdam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LynchVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(default=1)),
                ('game', models.ForeignKey(related_name=b'LynchVotes', to='wakkerdam.Game')),
                ('votee', models.ForeignKey(related_name=b'Votees', to='wakkerdam.Player')),
                ('voter', models.ForeignKey(related_name=b'Voters', to='wakkerdam.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
