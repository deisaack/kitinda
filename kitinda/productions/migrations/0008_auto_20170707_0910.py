# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0007_auto_20170707_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testsupply',
            old_name='conversation',
            new_name='supplied_by',
        ),
        migrations.RemoveField(
            model_name='testsupply',
            name='message',
        ),
    ]
