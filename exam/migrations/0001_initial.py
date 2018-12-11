# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameD', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameP', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.patient')),
            ],
        ),
    ]