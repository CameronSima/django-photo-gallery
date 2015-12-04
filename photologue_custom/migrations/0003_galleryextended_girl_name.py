# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue_custom', '0002_auto_20150121_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryextended',
            name='gallery_name',
            field=models.CharField(default='placeholder gallery name', max_length=50),
            preserve_default=False,
        ),
    ]
