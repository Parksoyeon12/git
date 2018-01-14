from django.shortcuts import render
from .models import School
import csv

# Create your views here.

def index(request):

    return render(request, 'myapp/index.html')



def input(request):

  line = []
  line1 = []

  f = open('장애인편의.csv', 'r')
  rdr = csv.reader(f)

  for row in rdr:
    line.insert(0,row)
    for lines in line:
      school = School(
        eduoffice = lines[0],
        code = lines[3],
        sname = lines[4],
        diff= lines[6],
        Enter  = lines[9],
        parking = lines[10],
        enhi  = lines[11],
        hallway = lines[12],
        hsupport = lines[13],
        hfeces = lines[14],
        hufine = lines[15],
        braille = lines[16],
        announce = lines[17],
        alarm = lines[18],
        address = lines[1],
        daddress = lines[2],
        pnum = lines[7],
        haddress = lines[5],
        sex = lines[8],
        )
      school.save()

  return render(request, 'myapp/index.html')
