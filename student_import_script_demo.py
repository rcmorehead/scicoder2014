#!/usr/bin/python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

filename = 'student_data.txt'

data = open(filename)

session = Session()

s = Student()
s.first_name = "Egon"
s.last_name = "Spengler"

session.add(s)

lacrosse = Club()
lacrosse.label = "lacrosse"
session.add(lacrosse)

s.clubs.append(lacrosse)

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)



