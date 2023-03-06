# Generated by Django 4.1.5 on 2023-03-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pravas', '0006_remove_user_profile_photo_alter_ticket_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbooking',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='destination',
            field=models.CharField(choices=[('Morbi', 'Morbi'), ('Navsari', 'Navsari'), ('Deesa', 'Deesa'), ('Mahesana', 'Mahesana'), ('Anand', 'Anand'), ('Vadodara', 'Vadodara'), ('Nadiad', 'Nadiad'), ('Rajkot', 'Rajkot'), ('Ahmedabad', 'Ahmedabad'), ('Jamnagar', 'Jamnagar'), ('Surat', 'Surat')], default='Ahmedabad', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='operators',
            field=models.CharField(choices=[('Tulsi', 'Tulsi'), ('Bharat', 'Bharat'), ('Kabra', 'Kabra'), ('GSRTC', 'GSRTC')], default='GSRTC', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='source',
            field=models.CharField(choices=[('Morbi', 'Morbi'), ('Navsari', 'Navsari'), ('Deesa', 'Deesa'), ('Mahesana', 'Mahesana'), ('Anand', 'Anand'), ('Vadodara', 'Vadodara'), ('Nadiad', 'Nadiad'), ('Rajkot', 'Rajkot'), ('Ahmedabad', 'Ahmedabad'), ('Jamnagar', 'Jamnagar'), ('Surat', 'Surat')], default='Ahmedabad', max_length=50),
        ),
    ]