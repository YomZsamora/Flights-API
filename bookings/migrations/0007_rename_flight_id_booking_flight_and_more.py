# Generated by Django 4.1.3 on 2022-12-14 12:31

import bookings.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_alter_passenger_email_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='flight_id',
            new_name='flight',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='passenger_id',
            new_name='passenger',
        ),
        migrations.AlterField(
            model_name='passenger',
            name='first_name',
            field=models.CharField(max_length=70, validators=[bookings.validators.validate_is_alpha]),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='last_name',
            field=models.CharField(max_length=70, validators=[bookings.validators.validate_is_alpha]),
        ),
    ]