# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue_custom', '0004_auto_20150122_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryextended',
            name='gallery_slug',
            field=models.SlugField(default='gallery-name-slug-placeholder'),
            preserve_default=False,
        ),
    ]
