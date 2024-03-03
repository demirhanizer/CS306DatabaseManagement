import mysql.connector
from faker import Faker
import random
from connect import create_connection

# Connect to your MySQL server
connection = create_connection()

# Create a cursor object
cursor = connection.cursor()

# Create a Faker instance
fake = Faker()

# Number of records to generate
num_records = 1050000

# Create a table
create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS Person (
        name VARCHAR(100),
        age INTEGER,
        gender VARCHAR(50),
        SSN VARCHAR(50),
        PRIMARY KEY(SSN)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Patient (
        Patient_SSN VARCHAR(50),
        emergency_contact VARCHAR(20),
        complaint VARCHAR(150),
        PRIMARY KEY(Patient_SSN),
        FOREIGN KEY (Patient_SSN) REFERENCES Person(SSN) ON DELETE CASCADE,
        INDEX idx_Patient_SSN (Patient_SSN)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Department (
        departmentID INTEGER,
        contactInformation VARCHAR(50),
        type VARCHAR(50),
        description VARCHAR(50),
        PRIMARY KEY(departmentID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Appointment (
        appointmentID INTEGER,
        appointmentTime DATE,
        location VARCHAR(100),
        PRIMARY KEY(appointmentID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Hospital (
        hospital_contactInformation VARCHAR(50),
        location VARCHAR(50),
        hospitalName VARCHAR(50),
        PRIMARY KEY(hospitalName)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Divides_Into (
        departmentID INTEGER NOT NULL,
        hospitalName VARCHAR(50),
        PRIMARY KEY(hospitalName, departmentID),
        FOREIGN KEY(hospitalName) REFERENCES Hospital(hospitalName) ON DELETE NO ACTION,
        FOREIGN KEY(departmentID) REFERENCES Department(departmentID) ON DELETE NO ACTION
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Doctor_WORKS_IN (
        profession VARCHAR(70),
        Doctor_SSN VARCHAR(50),
        experience INTEGER,
        hospitalName VARCHAR(50) NOT NULL,
        PRIMARY KEY(Doctor_SSN),
        FOREIGN KEY(Doctor_SSN) REFERENCES Person(SSN) ON DELETE NO ACTION,
        FOREIGN KEY(hospitalName) REFERENCES Hospital(hospitalName) ON DELETE NO ACTION,
        INDEX idx_hospitalName (hospitalName)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS AFFILIATE (
        Doctor_SSN CHAR(11),
        DepartmentID INTEGER,
        PRIMARY KEY(DepartmentID, Doctor_SSN),
        FOREIGN KEY(DepartmentID) REFERENCES Department(DepartmentID) ON DELETE NO ACTION,
        FOREIGN KEY(Doctor_SSN) REFERENCES Doctor_WORKS_IN(Doctor_SSN) ON DELETE NO ACTION,
        INDEX idx_Doctor_SSN (Doctor_SSN),
        INDEX idx_DepartmentID (DepartmentID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Appointment_SCHEDULES (
        Patient_SSN CHAR(11) NOT NULL,
        appointmentID INTEGER,
        appointmentTime DATE,
        location VARCHAR(100),
        FOREIGN KEY(Patient_SSN) REFERENCES Patient(Patient_SSN),
        PRIMARY KEY(appointmentID),
        INDEX idx_Patient_SSN (Patient_SSN)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS IS_ATTENDED_BY (
        appointmentID INTEGER,
        Doctor_SSN VARCHAR(50),
        PRIMARY KEY(appointmentID, Doctor_SSN),
        FOREIGN KEY(Doctor_SSN) REFERENCES Doctor_WORKS_IN(Doctor_SSN) ON DELETE NO ACTION,
        FOREIGN KEY(appointmentID) REFERENCES Appointment_SCHEDULES(appointmentID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Medical_Record_BELONGS_TO (
        recordID INTEGER NOT NULL,
        disease VARCHAR(100),
        date DATE,
        Patient_SSN CHAR(11) NOT NULL,
        FOREIGN KEY(Patient_SSN) REFERENCES Patient(Patient_SSN) ON DELETE NO ACTION,
        PRIMARY KEY(recordID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS CREATED_BY (
        recordID INTEGER,
        Doctor_SSN VARCHAR(50),
        PRIMARY KEY(recordID, Doctor_SSN),
        FOREIGN KEY(Doctor_SSN) REFERENCES Doctor_WORKS_IN(Doctor_SSN) ON DELETE NO ACTION,
        FOREIGN KEY(recordID) REFERENCES Medical_Record_BELONGS_TO(recordID) ON DELETE CASCADE
    )
    """
]

for query in create_table_queries:
    cursor.execute(query)

# Generate and insert data
existing_ssns = set()
cursor.execute("SELECT SSN FROM Person")
existing_records = cursor.fetchall()
existing_ssns.update(record[0] for record in existing_records)

# Generate and insert new records until reaching 1,000,000
while len(existing_ssns) < num_records:
    first_name = fake.first_name()
    ssn = fake.ssn()

    if ssn not in existing_ssns:
        gender = fake.random_element(elements=('Male', 'Female'))
        age = random.randint(18, 99)

        cursor.execute(
            """
            INSERT INTO Person (name, age, gender, SSN)
            VALUES (%s, %s, %s, %s)
            """,
            (first_name, age, gender, ssn),
        )

        existing_ssns.add(ssn)

print("Total records after insertion:", len(existing_ssns))

# Commit the changes
connection.commit()
'''
# Inserting into PATIENT table
for ssn in existing_ssns:
    cursor.execute(
        """
        INSERT INTO Patient (Patient_SSN)
        VALUES (%s)
        """,
        (ssn,)
    )
    connection.commit()  # Committing the changes
'''
'''
count = 0
while num_records > 0:
    hospital_contact = fake.phone_number()
    location = fake.city()
    hospital_name = fake.company()

    try:
        cursor.execute(
            """
            INSERT INTO Hospital (hospital_contactInformation, location, hospitalName)
            VALUES (%s, %s, %s)
            """,
            (hospital_contact, location, hospital_name),
        )
        connection.commit()  # Committing the changes
        #num_records -= 1  # Decrease the count on successful insertion
        count += 1
        if count == 1000111:
            break
    except mysql.connector.IntegrityError as e:
        # Handle duplicate entries by ignoring and continue generating new ones
        print(f"Duplicate entry: {hospital_name}. Ignoring and continuing...")

print("Total records inserted into Hospital table:", 1000000)
'''

# Inserting into DOCTOR_WORKSIN table
'''
cursor.execute("SELECT hospitalName FROM Hospital")
valid_hospital_names = [row[0] for row in cursor.fetchall()]

# Inserting into Doctor_WORKS_IN table
for ssn in existing_ssns:
    # Choose a random hospital name from the valid list
    doctor_hospital_name = random.choice(valid_hospital_names)

    cursor.execute(
        """
        INSERT INTO Doctor_WORKS_IN (Doctor_SSN, hospitalName)
        VALUES (%s, %s)
        """,
        (ssn, doctor_hospital_name)
    )
    connection.commit()  # Committing the changes
'''
count_dept = 0
count_appointment = 0

# Insert into Department table
while count_dept < num_records:
    department_id = fake.unique.random_int(min=1, max=num_records * 2)  # Adjust max range
    contact_info = fake.phone_number()
    dept_type = fake.word()
    description = fake.text(max_nb_chars=50)

    try:
        cursor.execute(
            """
            INSERT INTO Department (departmentID, contactInformation, type, description)
            VALUES (%s, %s, %s, %s)
            """,
            (department_id, contact_info, dept_type, description),
        )
        connection.commit()
        if count_dept == num_records:
            break

        count_dept += 1
    except mysql.connector.IntegrityError as e:
        connection.rollback()
        # Handle duplicate entries by continuing
        print(f"Duplicate entry in Department table. Ignoring and continuing...")

# Insert into Appointment table
while count_appointment < num_records:
    appointment_id = fake.unique.random_int(min=1, max=num_records * 2)  # Adjust max range
    appointment_time = fake.date_this_decade()
    location = fake.address()

    try:
        cursor.execute(
            """
            INSERT INTO Appointment (appointmentID, appointmentTime, location)
            VALUES (%s, %s, %s)
            """,
            (appointment_id, appointment_time, location),
        )
        connection.commit()
        if count_appointment == num_records:
            break
            
        count_appointment += 1
    except mysql.connector.IntegrityError as e:
        connection.rollback()
        # Handle duplicate entries by continuing
        print(f"Duplicate entry in Appointment table. Ignoring and continuing...")

print("Total records inserted into Department table:", count_dept)
print("Total records inserted into Appointment table:", count_appointment)




# Close the cursor and connection
cursor.close()
connection.close()
