# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_stormpath.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='StormpathUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, verbose_name=b'ID')),
                ('href', models.CharField(max_length=255, null=True, blank=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('given_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address', db_index=True)),
                ('is_active', models.BooleanField(default=django_stormpath.models.get_default_is_active)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
