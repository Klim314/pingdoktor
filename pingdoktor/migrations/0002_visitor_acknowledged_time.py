# Generated by Django 2.0.6 on 2018-09-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingdoktor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='acknowledged_time',
            field=models.DateTimeField(null=True),
        ),
    ]
