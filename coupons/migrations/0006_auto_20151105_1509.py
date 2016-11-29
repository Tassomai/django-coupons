# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_auto_20151105_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='redeemed_at',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='user',
        ),
    ]
