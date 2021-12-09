# Generated by Django 3.2 on 2021-12-09 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1550)),
                ('estimated_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('age_range', models.CharField(choices=[('0-1', '0-1'), ('1-3', '1-3'), ('3-5', '3-5'), ('6-7', '6-7'), ('7-10', '7-10'), ('10-13', '10-13'), ('13-16', '13-16')], max_length=25)),
                ('needed', models.BooleanField(default=True)),
                ('committed', models.BooleanField(default=False)),
                ('commited_by', models.CharField(blank=True, max_length=150, null=True)),
                ('received', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]