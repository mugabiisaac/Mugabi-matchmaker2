# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employermatch',
            name='employer',
            field=models.ForeignKey(default=False, to='jobs.Employer'),
        ),
        migrations.AddField(
            model_name='locationmatch',
            name='location',
            field=models.ForeignKey(default=False, to='jobs.Location'),
        ),
        migrations.AddField(
            model_name='positionmatch',
            name='job',
            field=models.ForeignKey(default=False, to='jobs.Job'),
        ),
    ]
