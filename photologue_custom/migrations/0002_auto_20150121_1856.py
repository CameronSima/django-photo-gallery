# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue_custom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryextended',
            options={'verbose_name': 'Extra field', 'verbose_name_plural': 'Extra fields'},
        ),
    ]
