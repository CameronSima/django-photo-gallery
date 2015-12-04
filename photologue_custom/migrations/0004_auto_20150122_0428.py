# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue_custom', '0003_galleryextended_girl_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryextended',
            name='gallery',
            field=models.OneToOneField(related_name='galleryextended', to='photologue.Gallery'),
            preserve_default=True,
        ),
    ]
