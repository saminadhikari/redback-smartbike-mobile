# Generated by Django 4.2.11 on 2024-04-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0015_helpcentremessage_terminateaccountmessage_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_created',
            field=models.DateTimeField(null=True),
        ),
    ]
