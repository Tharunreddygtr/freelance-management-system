# Generated by Django 4.0.5 on 2022-09-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0003_remove_client_details_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_jobs',
            name='experience_level',
            field=models.CharField(max_length=100),
        ),
    ]
