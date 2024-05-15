# Generated by Django 4.2.4 on 2023-08-25 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_memberdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_1',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_2',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_3',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_4',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_5',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
