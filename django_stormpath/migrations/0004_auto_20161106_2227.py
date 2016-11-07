# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_stormpath', '0003_auto_20160426_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stormpathuser',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, verbose_name=b'ID'),
        ),
    ]
