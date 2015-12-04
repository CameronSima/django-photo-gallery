# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('photologue', '0006_auto_20141028_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryExtended',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gallery', models.OneToOneField(related_name='extend', to='photologue.Gallery')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Extra fields',
                'verbose_name_plural': 'Extra fields',
            },
            bases=(models.Model,),
        ),
    ]
