# Generated by Django 3.2 on 2021-12-14 13:49

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organisation_name', models.CharField(max_length=150, unique=True)),
                ('type', models.CharField(choices=[('charity', 'CHARITY'), ('donor', 'DONOR')], max_length=25)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CharityAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=150)),
                ('address_line_one', models.CharField(max_length=150)),
                ('address_line_two', models.CharField(blank=True, max_length=150, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=150, null=True)),
                ('county', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('postcode', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
