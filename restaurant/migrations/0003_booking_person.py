# Generated by Django 2.0.2 on 2018-10-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.CharField(default=1, max_length=120),
        ),
    ]
