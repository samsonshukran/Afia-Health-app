-- Drop old tables if they exist
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS anc;
DROP TABLE IF EXISTS cwc;
DROP TABLE IF EXISTS immunization;
DROP TABLE IF EXISTS surveillance;

-- Patients table
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    contact TEXT
);

-- ANC table
CREATE TABLE anc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mother_name TEXT NOT NULL,
    visit_date TEXT,
    status TEXT
);

-- CWC table
CREATE TABLE cwc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_name TEXT NOT NULL,
    age INTEGER,
    checkup_date TEXT
);

-- Immunization table
CREATE TABLE immunization (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_name TEXT NOT NULL,
    vaccine TEXT,
    date TEXT
);

-- Surveillance table
CREATE TABLE surveillance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease TEXT NOT NULL,
    cases INTEGER,
    report_date TEXT
);

-- Insert sample Patients
INSERT INTO patients (name, age, gender, contact) VALUES
('John Doe', 32, 'Male', '0700123456'),
('Jane Smith', 28, 'Female', '0712345678'),
('Ali Hassan', 45, 'Male', '0723456789');

-- Insert sample ANC
INSERT INTO anc (mother_name, visit_date, status) VALUES
('Mary Atieno', '2025-08-15', 'First Visit'),
('Sarah Wanjiku', '2025-08-20', 'Follow-up'),
('Fatuma Abdalla', '2025-08-25', 'Completed');

-- Insert sample CWC
INSERT INTO cwc (child_name, age, checkup_date) VALUES
('Kevin Otieno', 2, '2025-08-10'),
('Grace Njeri', 1, '2025-08-18'),
('Aisha Mohamed', 3, '2025-08-22');

-- Insert sample Immunization
INSERT INTO immunization (child_name, vaccine, date) VALUES
('Kevin Otieno', 'BCG', '2025-08-05'),
('Grace Njeri', 'Polio', '2025-08-12'),
('Aisha Mohamed', 'Measles', '2025-08-19');

-- Insert sample Surveillance
INSERT INTO surveillance (disease, cases, report_date) VALUES
('Malaria', 15, '2025-08-01'),
('Cholera', 5, '2025-08-10'),
('COVID-19', 20, '2025-08-15');
