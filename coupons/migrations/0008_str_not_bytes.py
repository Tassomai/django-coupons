# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0007_auto_20151105_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='campaign',
            field=models.ForeignKey(related_name='coupons', verbose_name='Campaign', blank=True, to='coupons.Campaign', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Type', choices=[(b'monetary', b'Money based coupon'), (b'percentage', b'Percentage discount'), (b'virtual_currency', b'Virtual currency')])
        )
    ]
