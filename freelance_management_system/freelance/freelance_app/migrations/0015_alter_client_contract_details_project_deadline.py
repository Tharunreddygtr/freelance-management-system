# Generated by Django 4.0.5 on 2022-10-11 06:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0014_alter_client_contract_details_project_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_contract_details',
            name='project_deadline',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]