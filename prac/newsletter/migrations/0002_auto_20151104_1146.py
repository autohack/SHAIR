# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151011102433 on 2015-11-04 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Date_of_birth',
            new_name='Date_of_Birth',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='full_name',
            new_name='Full_Name',
        ),
    ]