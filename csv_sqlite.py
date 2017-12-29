############ All you need to modify is below ############
# Full path and name to your csv file
csv_filepathname="/media/sf_KBase/CricTrack/Django/CC/proj_cc/app_dob2/deck_data.csv"
# Full path to the directory immediately above your django project directory
your_djangoproject_home="/media/sf_KBase/CricTrack/Django/CC/"
############ All you need to modify is above ############

proj_folder = "/media/sf_KBase/CricTrack/Django/CC/proj_cc/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='proj_cc.settings'

import django
django.setup()

from proj_cc.app_dob2.models import mt_game

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

old_school = None
for row in dataReader:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    
    
    if old_school != row[4]:
        old_school = row[4]
        school = School()
        school.name = old_school
        school.save()

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    lawyer=Lawyer()
    lawyer.firm_url=row[0]
    lawyer.firm_name=row[1]
    lawyer.first=row[2]
    lawyer.last=row[3]

    lawyer_school=School.objects.get(name=row[4])
    lawyer.school=lawyer_school

    lawyer.year_graduated=row[5]
    lawyer.save()