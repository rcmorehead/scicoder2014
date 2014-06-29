#!/usr/bin/python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

filename = 'student_data.txt'

data = open(filename)
lines = data.readlines()
data.close()

session = Session()

for line in lines[5:]:
	line = line.split("|")
	#print line

	try: 
		a_student = session.query(Student).filter(Student.last_name==line[1]).filter(Student.first_name==line[0]).one()
		
	except sqlalchemy.orm.exc.NoResultFound:								   
		student = Student()
		student.first_name = line[0]
		student.last_name = line[1]
	
	
		session.add(student)
		print("Adding {} {}".format(line[0],line[1])) 

	except sqlalchemy.orm.exc.MultipleResultsFound:
		print("**{} {} is already in database!**".format(line[0],line[1])) 

#Eccleston/Room 205, Baker/Room 315
	supers = line[3].split(',')

	for supe in supers:
		supe = supe.split('/')

		if len(supe) < 2 :
			continue

		supe[0].strip(' ')

		try:
			one_supervisor = session.query(Supervisor).filter(Supervisor.last_name==supe[0]) \
											  .filter(Supervisor.room_number==supe[1]).one()
		except sqlalchemy.orm.exc.NoResultFound:
			one_supervisor = Supervisor()
			one_supervisor.last_name = supe[0]
 			one_supervisor.first_name = ""
 			one_supervisor.room_number = supe[1]

 			session.add(one_supervisor)
		except sqlalchemy.orm.exc.MultipleResultsFound:
 			print "There is more than one Doctor!"
 			sys.exit(1)
	
	student.supervisors.append(one_supervisor)

	

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)
