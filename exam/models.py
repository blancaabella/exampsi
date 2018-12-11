# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify
import django
import datetime

# Create your models here.

class patient(models.Model):
    nameP = models.CharField( max_length=128)

class doctor(models.Model):
    nameD = models.CharField(max_length=128)

class prescription(models.Model):
    doctorId = models.ForeignKey(doctor, null=True)
    patientId= models.ForeignKey(patient, null=True)
