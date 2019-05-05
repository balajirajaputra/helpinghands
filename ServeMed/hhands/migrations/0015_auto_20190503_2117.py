# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-03 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhands', '0014_merge_20190503_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhutilization',
            name='quarter_begin',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dhutilization',
            name='quarter_begin_date',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='mcd_amt_reimbursed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='non_mcd_amt_reimbursed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='s_latitude',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='s_longitude',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='total_amt_reimbursed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='units_reimbursed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]