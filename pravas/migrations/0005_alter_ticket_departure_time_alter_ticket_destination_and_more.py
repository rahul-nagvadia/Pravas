# Generated by Django 4.1.5 on 2023-02-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pravas', '0004_alter_ticket_destination_alter_ticket_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='destination',
            field=models.CharField(choices=[('Vadodara', 'Vadodara'), ('Nadiad', 'Nadiad'), ('Morbi', 'Morbi'), ('Surat', 'Surat'), ('Mahesana', 'Mahesana'), ('Jamnagar', 'Jamnagar'), ('Navsari', 'Navsari'), ('Ahmedabad', 'Ahmedabad'), ('Rajkot', 'Rajkot'), ('Deesa', 'Deesa'), ('Anand', 'Anand')], default='Ahmedabad', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='mode',
            field=models.CharField(choices=[('Plane', 'Plane'), ('Bus', 'Bus'), ('Train', 'Train')], default='Bus', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='operators',
            field=models.CharField(choices=[('Kabra', 'Kabra'), ('GSRTC', 'GSRTC'), ('Tulsi', 'Tulsi'), ('Bharat', 'Bharat')], default='GSRTC', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='source',
            field=models.CharField(choices=[('Vadodara', 'Vadodara'), ('Nadiad', 'Nadiad'), ('Morbi', 'Morbi'), ('Surat', 'Surat'), ('Mahesana', 'Mahesana'), ('Jamnagar', 'Jamnagar'), ('Navsari', 'Navsari'), ('Ahmedabad', 'Ahmedabad'), ('Rajkot', 'Rajkot'), ('Deesa', 'Deesa'), ('Anand', 'Anand')], default='Ahmedabad', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='total_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='date_booked',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tourbooking',
            name='date_booked',
            field=models.DateTimeField(),
        ),
    ]
