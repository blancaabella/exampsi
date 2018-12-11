#populate database
# This code has to be placed in a file within the
# data/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# so let's call it populate.py. Another thing that has to be done
# is creating __init__.py files in both the management and commands
# directories, because these have to be Python packages.
#
# execute python manage.py  populate

import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sampleTest.settings')
import django
django.setup()

from exam.models import doctor, patient, prescription
#models

# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly

for i in range(1,4):
    d = doctor.objects.get_or_create(id=i)[0]
    d.nameD = 'doctor' + str(i)
    d.save()

for i in range(1,2):
    p = patient.objects.get_or_create(id = i)[0]
    p.nameP = 'patient' + str(i)
    p.save()

l=[(1, 1, 1), (2, 2, 1), (3, 1, 2), (4, 2, 2), (5, 3, 2)]
for i in range(len(l)):
    pr = prescription.objects.get_or_create(id = l[i][0])[0]
    pr.doctorId = l[i][1]
    pr.patientId = l[i][2]
    pr.save()
