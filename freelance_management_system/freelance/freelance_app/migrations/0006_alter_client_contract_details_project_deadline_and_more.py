# Generated by Django 4.0.5 on 2022-09-29 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0005_alter_client_contract_details_project_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_contract_details',
            name='project_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 11, 52, 13, 631590)),
        ),
        migrations.AlterField(
            model_name='client_contract_details',
            name='project_status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]