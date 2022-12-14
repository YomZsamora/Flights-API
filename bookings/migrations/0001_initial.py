# Generated by Django 4.1.3 on 2022-11-08 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=50)),
                ('to_location', models.CharField(max_length=50)),
                ('departure_time', models.DateTimeField(auto_now_add=True)),
                ('arrival_time', models.DateTimeField(auto_now=True)),
                ('available_seats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=70)),
                ('first_name', models.CharField(max_length=70)),
                ('email_address', models.CharField(max_length=70, unique=True)),
                ('phone_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_seat', models.CharField(max_length=3)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.flight')),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.passenger')),
            ],
        ),
    ]
