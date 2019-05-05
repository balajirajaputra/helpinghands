# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-13 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhands', '0006_auto_20190312_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhutilization',
            name='m_dr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drugs_utilization', to='hhands.DrugsHeader'),
        ),
        migrations.AlterField(
            model_name='drreimbursements',
            name='dr_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drugs_reimbursements', to='hhands.DHUtilization'),
        ),
    ]