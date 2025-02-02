# Generated by Django 4.2.4 on 2023-08-27 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_memberlastcompletehistory_session_one_completed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberlastcompletehistory',
            name='session_one_completed',
        ),
        migrations.RemoveField(
            model_name='memberlastcompletehistory',
            name='session_three_completed',
        ),
        migrations.RemoveField(
            model_name='memberlastcompletehistory',
            name='session_two_completed',
        ),
        migrations.AddField(
            model_name='memberlastcompletehistory',
            name='session_complete_1',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 27, 15, 10, 13, 65861), null=True),
        ),
        migrations.AddField(
            model_name='memberlastcompletehistory',
            name='session_complete_2',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 27, 15, 10, 13, 65861), null=True),
        ),
        migrations.AddField(
            model_name='memberlastcompletehistory',
            name='session_complete_3',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 27, 15, 10, 13, 65861), null=True),
        ),
    ]
