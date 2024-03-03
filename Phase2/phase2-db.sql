create table Divides_Into(
    departmentID INTEGER NOT NULL,
    hospitalName VARCHAR(50),
    PRIMARY KEY(hospitalName, departmentID),
    FOREIGN KEY(hospitalName) REFERENCES Hospital(hospitalName) ON DELETE NO
    ACTION,
    FOREIGN KEY(departmentID) REFERENCES Department(departmentID) ON DELETE NO ACTION
);


create table Doctor_WORKS_IN (
    profession VARCHAR(70),
    Doctor_SSN VARCHAR(50),
    experience INTEGER,
    hospitalName VARCHAR(50) NOT NULL,
    PRIMARY KEY(Doctor_SSN),
    FOREIGN KEY(Doctor_SSN) REFERENCES Person(SSN) ON DELETE NO ACTION,
    FOREIGN KEY(hospitalName) REFERENCES Hospital(hospitalName) ON DELETE NO ACTION
);

insert into Hospital values("+90 216 578 58 66", "Kadikoy", "Acıbadem Kadikoy");
insert into Hospital values("+90 212 444 58 66", "Maslak", "Acıbadem Maslak");
insert into Hospital values("+90 212 338 58 66", "Zeytinburnu", "Koç University Hospital");
insert into Hospital values("+90 212 655 58 66", "Avcılar", "Istanbul University Cerrahpaşa Faculty of Medicine");
insert into Hospital values("+90 212 782 58 66", "Avcılar", "Istanbul University Istanbul Faculty of Medicine");
insert into Hospital values("+90 216 986 58 66", "Altunizade", "Academic Hospital");
insert into Hospital values("+90 212 233 58 66", "Yesilkoy", "Acıbadem International Hospital");
insert into Hospital values("+90 216 120 58 66", "Bakırkoy", "Acıbadem Bakırkoy");
insert into Hospital values("+90 216 132 58 66", "Nisantasi", "American Hospital");
insert into Hospital values("+90 216 154 58 66", "Avcılar", "Avcılar Hospital");

insert into Department values("1","+90 216 578 58 66","1","Cardiology");
insert into Department values("2","+90 212 444 58 66","2","Dermatology");
insert into Department values("3","+90 212 338 58 66","3","Endocrinology");
insert into Department values("4","+90 212 655 58 66","4","Gastroenterology");
insert into Department values("5","+90 212 782 58 66","5","Hematology");
insert into Department values("6","+90 216 986 58 66","6","Infectious Disease");
insert into Department values("7","+90 212 233 58 66","7","Nephrology");
insert into Department values("8","+90 216 120 58 66","8","Neurology");
insert into Department values("9","+90 216 132 58 66","9","Oncology");
insert into Department values("10","+90 216 154 58 66","10","Orthopedics");

insert into Divides_Into values("1", "Acıbadem Kadikoy");
insert into Divides_Into values("2", "Acıbadem Maslak");
insert into Divides_Into values("3", "Koç University Hospital");
insert into Divides_Into values("4", "Istanbul University Cerrahpaşa Faculty of Medicine");
insert into Divides_Into values("5", "Istanbul University Istanbul Faculty of Medicine");
insert into Divides_Into values("6", "Academic Hospital");
insert into Divides_Into values("7", "Acıbadem International Hospital");
insert into Divides_Into values("8", "Acıbadem Bakırkoy");
insert into Divides_Into values("9", "American Hospital");
insert into Divides_Into values("10", "Avcılar Hospital");

insert into person values('Demirhan Izer ', '27' ,'M','253 888 55 355');
insert into person values('Kadir Izer','22','M','987 654 32 109');
insert into person values('Ilter Akgun','19','M','567 890 12 345');
insert into person values('Utku Akgun','32','M','876 543 21 098');
insert into person values('Kerem Kiranbagli','47','M','234 567 89 012');
insert into person values('Mert Coskuner','55','M','789 012 34 567');
insert into person values('Emre Coskuner','33','M','456 789 01 234');
insert into person values('Ahmet Emre Eser ','22','M','345 678 90 123');
insert into person values('Erdem Ozcan','63','M','210 987 65 432');
insert into person values('Faruk Kara','11','M','654 321 09 876');

insert into Doctor_WORKS_IN values("Cardiology", "253 888 55 355","1", "Acıbadem Kadikoy");
insert into Doctor_WORKS_IN values("Cardiology", "987 654 32 109","2", "Acıbadem Kadikoy");
insert into Doctor_WORKS_IN values("Endocrinology", "567 890 12 345","3", "Koç University Hospital");
insert into Doctor_WORKS_IN values("Gastroenterology", "876 543 21 098","4", "Istanbul University Cerrahpaşa Faculty of Medicine");
insert into Doctor_WORKS_IN values("Hematology", "234 567 89 012","5", "Istanbul University Istanbul Faculty of Medicine");
insert into Doctor_WORKS_IN values("Infectious Disease", "789 012 34 567","6", "Academic Hospital");
insert into Doctor_WORKS_IN values("Nephrology", "456 789 01 234","7", "Acıbadem International Hospital");
insert into Doctor_WORKS_IN values("Neurology", "345 678 90 123","8", "Acıbadem Bakırkoy");
insert into Doctor_WORKS_IN values("Oncology", "210 987 65 432","9", "American Hospital");
insert into Doctor_WORKS_IN values("Orthopedics", "654 321 09 876","10", "Avcılar Hospital");

SELECT DWI.DoctorSSN
FROM Hospital_Divides_Into AS HDI ,Doctor_WORKS_IN AS DWI
WHERE HDI.hospitalName = 'American Hospital' AND DWI.profession ='Oncology';

SELECT DI.hospitalName, AVG(DWI.experience)
FROM Divides_Into AS DI, Doctor_WORKS_IN AS DWI
WHERE DWI.hospitalName = DI.hospitalName
GROUP BY DI.hospitalName;


ALTER TABLE Doctor_WORKS_IN
ADD CONSTRAINT DOCTOR_EXPERIENCE
CHECK (
hospitalName IN (SELECT HDI.hospitalName
FROM Divides_Into HDI, Doctor_WORKS_IN DWI
WHERE DWI.hospitalName = HDI.hospitalName)
);