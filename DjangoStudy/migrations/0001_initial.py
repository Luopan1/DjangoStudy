# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gName', models.CharField(max_length=20)),
                ('gUpDate', models.DateTimeField()),
                ('gDownDate', models.DateTimeField()),
                ('gIsDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sName', models.CharField(max_length=20)),
                ('sAddress', models.CharField(max_length=40)),
                ('sType', models.CharField(max_length=20)),
                ('sOpenTime', models.DateTimeField()),
                ('sCloseTime', models.DateTimeField()),
                ('sIsDelete', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='shop',
            field=models.ForeignKey(to='DjangoStudy.ShopInfo'),
        ),
    ]
