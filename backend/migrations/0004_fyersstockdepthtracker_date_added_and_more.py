# Generated by Django 4.0.5 on 2022-08-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_fyersstockdepthtracker_fyersstocktracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='fyersstockdepthtracker',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fyersstocktracker',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
