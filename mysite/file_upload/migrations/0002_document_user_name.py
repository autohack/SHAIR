# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user_name',
            field=models.CharField(default=b'PUBLIC', max_length=100),
        ),
    ]
