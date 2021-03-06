# Generated by Django 2.1.2 on 2018-10-09 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('d92ab193-395f-4b24-8f0c-4d2cd2884bb8'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2018, 10, 9, 18, 53, 52, 216125, tzinfo=utc))),
                ('dueDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.UUID('ceca57ce-c373-4d42-b8aa-bfd9bfcead70'), editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
