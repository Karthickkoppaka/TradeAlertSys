# Generated by Django 4.0.5 on 2022-08-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_fyersstockdepthtracker_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fyersstockdepthtracker',
            name='timestamp',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
