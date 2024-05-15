# Generated by Django 4.2.4 on 2023-08-25 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_memberdata_completed_stage_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberdata',
            name='completed_stage_2',
        ),
        migrations.RemoveField(
            model_name='memberdata',
            name='completed_stage_3',
        ),
        migrations.RemoveField(
            model_name='memberdata',
            name='completed_stage_4',
        ),
        migrations.RemoveField(
            model_name='memberdata',
            name='completed_stage_5',
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='completed_stage_1',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
