# Generated by Django 4.0.5 on 2022-10-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_app', '0015_alter_client_contract_details_project_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_feedback_form',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='freelancer_feedback_form',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
