# Generated by Django 4.1.5 on 2023-03-29 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('type', models.CharField(choices=[('EC', 'EC'), ('1AC', '1AC'), ('2AC', '2AC'), ('3AC', '3AC'), ('FC', 'FC'), ('CC', 'CC'), ('SL', 'SL'), ('2S', '2S')], default='2S', max_length=10)),
                ('prize', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoachAllocation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.coach')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeatAllocation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coachAllocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.coachallocation')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateField()),
                ('seat_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.seatallocation')),
                ('train_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sequence', models.PositiveIntegerField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('distance', models.IntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
            ],
        ),
        migrations.CreateModel(
            name='RunDays',
            fields=[
                ('day', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('train', models.ManyToManyField(to='train.train')),
            ],
        ),
        migrations.AddField(
            model_name='coachallocation',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train'),
        ),
    ]