# Generated by Django 4.0.5 on 2022-09-30 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0007_client_contract_details_contract_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_contract_details',
            name='contract_amount',
        ),
        migrations.AlterField(
            model_name='client_contract_details',
            name='project_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 4, 13, 55, 645341)),
        ),
    ]
