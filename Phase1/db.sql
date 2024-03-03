DROP DATABASE IF EXISTS cs306projev1;

CREATE DATABASE cs306projev1;

USE cs306projev1;

create table
    Person (
        name VARCHAR(100),
        age INTEGER,
        gender VARCHAR(50),
        SSN VARCHAR(50),
        PRIMARY KEY (SSN)
    );

create table
    Patient (
        Patient_SSN VARCHAR(50),
        emergency_contact VARCHAR(20),
        complaint VARCHAR(150),
        PRIMARY KEY (Patient_SSN),
        FOREIGN KEY (Patient_SSN) REFERENCES Person (SSN) ON DELETE CASCADE
    );

create table
    Department (
        departmentID INTEGER,
        contactInformation VARCHAR(50),
        type VARCHAR(50),
        description VARCHAR(50),
        PRIMARY KEY (departmentID)
    );

create table
    Appointment (
        appointmentID INTEGER,
        appointmentTime DATE,
        location VARCHAR(100),
        PRIMARY KEY (appointmentID)
    );

create table
    Hospital (
        hospital_contactInformation VARCHAR(50),
        location VARCHAR(50),
        hospitalName VARCHAR(50),
        PRIMARY KEY (hospitalName)
    );

create table
    Divides_Into (
        departmentID INTEGER NOT NULL,
        hospitalName VARCHAR(50),
        PRIMARY KEY (hospitalName, departmentID),
        FOREIGN KEY (hospitalName) REFERENCES Hospital (hospitalName) ON DELETE NO ACTION,
        FOREIGN KEY (departmentID) REFERENCES Department (departmentID) ON DELETE NO ACTION
    );

create table
    Doctor_WORKS_IN (
        profession VARCHAR(70),
        Doctor_SSN VARCHAR(50),
        experience INTEGER,
        hospitalName VARCHAR(50) NOT NULL,
        PRIMARY KEY (Doctor_SSN),
        FOREIGN KEY (Doctor_SSN) REFERENCES Person (SSN) ON DELETE NO ACTION,
        FOREIGN KEY (hospitalName) REFERENCES Hospital (hospitalName) ON DELETE NO ACTION
    );

create table
    AFFILIATE (
        Doctor_SSN CHAR(11),
        DepartmentID INTEGER,
        PRIMARY KEY (DepartmentID, Doctor_SSN),
        FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID) ON DELETE NO ACTION,
        FOREIGN KEY (Doctor_SSN) REFERENCES Doctor_WORKS_IN (Doctor_SSN) ON DELETE NO ACTION
    );

create table
    Appointment_SCHEDULES (
        Patient_SSN CHAR(11) NOT NULL,
        appointmentID INTEGER,
        appointmentTime DATE,
        location VARCHAR(100),
        FOREIGN KEY (Patient_SSN) REFERENCES Patient (Patient_SSN),
        PRIMARY KEY (appointmentID)
    );

create table
    IS_ATTENDED_BY (
        appointmentID INTEGER,
        Doctor_SSN VARCHAR(50),
        PRIMARY KEY (appointmentID, Doctor_SSN),
        FOREIGN KEY (Doctor_SSN) REFERENCES Doctor_WORKS_IN (Doctor_SSN) ON DELETE NO ACTION,
        FOREIGN KEY (appointmentID) REFERENCES Appointment_SCHEDULES (appointmentID)
    );

create table
    Medical_Record_BELONGS_TO (
        recordID INTEGER NOT NULL,
        disease VARCHAR(100),
        date DATE,
        Patient_SSN CHAR(11) NOT NULL,
        FOREIGN KEY (Patient_SSN) REFERENCES Patient (Patient_SSN) ON DELETE NO ACTION,
        PRIMARY KEY (recordID)
    );

create table
    CREATED_BY (
        recordID INTEGER,
        Doctor_SSN VARCHAR(50),
        PRIMARY KEY (recordID, Doctor_SSN),
        FOREIGN KEY (Doctor_SSN) REFERENCES Doctor_WORKS_IN (Doctor_SSN) ON DELETE NO ACTION,
        FOREIGN KEY (recordID) REFERENCES Medical_Record_BELONGS_TO (recordID) ON DELETE CASCADE
    );
