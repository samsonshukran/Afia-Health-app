from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "health-app.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- Dashboard ----------------
@app.route('/')
def dashboard():
    conn = get_db_connection()

    patients = conn.execute("SELECT * FROM patients").fetchall()
    anc = conn.execute("SELECT * FROM anc").fetchall()
    cwc = conn.execute("SELECT * FROM cwc").fetchall()
    immunization = conn.execute("SELECT * FROM immunization").fetchall()
    surveillance = conn.execute("SELECT * FROM surveillance").fetchall()

    conn.close()
    return render_template(
        "dashboard.html",
        patients=patients,
        anc=anc,
        cwc=cwc,
        immunization=immunization,
        surveillance=surveillance
    )

# ---------------- Patients ----------------
@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    contact = request.form['contact']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO patients (name, age, gender, contact) VALUES (?, ?, ?, ?)",
        (name, age, gender, contact)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# ---------------- ANC ----------------
@app.route('/add_anc', methods=['POST'])
def add_anc():
    mother_name = request.form['mother_name']
    visit_date = request.form['visit_date']
    status = request.form['status']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO anc (mother_name, visit_date, status) VALUES (?, ?, ?)",
        (mother_name, visit_date, status)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# ---------------- CWC ----------------
@app.route('/add_cwc', methods=['POST'])
def add_cwc():
    child_name = request.form['child_name']
    age = request.form['age']
    checkup_date = request.form['checkup_date']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO cwc (child_name, age, checkup_date) VALUES (?, ?, ?)",
        (child_name, age, checkup_date)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# ---------------- Immunization ----------------
@app.route('/add_immunization', methods=['POST'])
def add_immunization():
    child_name = request.form['child_name']
    vaccine = request.form['vaccine']
    date = request.form['date']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO immunization (child_name, vaccine, date) VALUES (?, ?, ?)",
        (child_name, vaccine, date)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# ---------------- Surveillance ----------------
@app.route('/add_surveillance', methods=['POST'])
def add_surveillance():
    disease = request.form['disease']
    cases = request.form['cases']
    report_date = request.form['report_date']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO surveillance (disease, cases, report_date) VALUES (?, ?, ?)",
        (disease, cases, report_date)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
