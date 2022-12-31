--
-- File generated with SQLiteStudio v3.4.1 on Wed Dec 28 21:09:51 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: careerJournal_employment
DROP TABLE IF EXISTS careerJournal_employment;
CREATE TABLE IF NOT EXISTS "careerJournal_employment" ("EmployeeId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "EmployeeName" varchar(500) NOT NULL, "EmployeeTitle" varchar(500) NOT NULL, "DateOfJoining" date NOT NULL, "PhotoFileName" varchar(500) NULL);

-- Table: careerJournal_users
DROP TABLE IF EXISTS careerJournal_users;
CREATE TABLE IF NOT EXISTS "careerJournal_users" ("UserId" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "UserName" varchar(500) NOT NULL, "UserEmail" varchar(100) NOT NULL, "UserProfile" varchar(500) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
