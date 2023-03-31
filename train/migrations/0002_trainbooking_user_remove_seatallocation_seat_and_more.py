# Generated by Django 4.1.5 on 2023-03-30 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainbooking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='seatallocation',
            name='seat',
        ),
        migrations.AddField(
            model_name='seatallocation',
            name='seat',
            field=models.ManyToManyField(to='train.seat'),
        ),
    ]