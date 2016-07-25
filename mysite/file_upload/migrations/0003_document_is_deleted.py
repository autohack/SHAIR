# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_document_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_deleted',
            field=models.IntegerField(default=0),
        ),
    ]
