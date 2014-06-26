CREATE TABLE "city" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT NOT NULL );
CREATE TABLE "club" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT);
CREATE TABLE "status" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT NOT NULL );
CREATE TABLE "student" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "first_name" TEXT NOT NULL , "last_name" TEXT NOT NULL , "city_id" INTEGER NOT NULL , "status_id" INTEGER NOT NULL );
CREATE TABLE "student_to_club" ("student_id" INTEGER NOT NULL , "club_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "club_id"));
CREATE TABLE "student_to_supervisor" ("student_id" INTEGER NOT NULL , "supervisor_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "supervisor_id"));
CREATE TABLE "supervisor" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "first_name" TEXT NOT NULL , "last_name" TEXT NOT NULL , "room_number" TEXT);
