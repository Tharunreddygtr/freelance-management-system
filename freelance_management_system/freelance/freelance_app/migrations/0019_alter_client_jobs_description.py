# Generated by Django 4.0.5 on 2022-10-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0018_alter_freelancer_proposals_proprosal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_jobs',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
