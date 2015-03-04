# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wakkerdam', '0002_auto_20150304_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wolfvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(default=1)),
                ('game', models.ForeignKey(related_name=b'WolfVotes', to='wakkerdam.Game')),
                ('votee', models.ForeignKey(related_name=b'Wolfvotees', to='wakkerdam.Player')),
                ('voter', models.ForeignKey(related_name=b'Wolfvoters', to='wakkerdam.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
