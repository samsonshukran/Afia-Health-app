// === Utility: Save data in localStorage ===
function saveData(key, record) {
  let data = JSON.parse(localStorage.getItem(key)) || [];
  data.push(record);
  localStorage.setItem(key, JSON.stringify(data));
}

// === Utility: Load data from localStorage ===
function loadData(key) {
  return JSON.parse(localStorage.getItem(key)) || [];
}

// === Show selected tab ===
function showTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(tab => tab.style.display = "none");
  document.getElementById(tabId).style.display = "block";

  if (tabId === 'dashboard') loadDashboard();
}

// === Show selected form ===
function showForm(formId) {
  document.querySelectorAll('.form-container').forEach(f => f.style.display = "none");
  document.getElementById(formId).style.display = "block";

  document.querySelectorAll('.form-desc').forEach(desc => desc.classList.remove('active'));
  document.getElementById(formId + 'Desc').classList.add('active');
}

// === Prevent default submit + persist data ===
document.querySelectorAll("form").forEach(form => {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formId = this.id;
    const formData = {};
    new FormData(this).forEach((value, key) => formData[key] = value);

    saveData(formId, formData);
    alert("Form submitted successfully!");
    this.reset();
    loadDashboard();
  });
});

// === Load Dashboard ===
function loadDashboard() {
  // Helper: populate tables
  function populateTable(tableId, records, columns) {
    const tbody = document.querySelector(`#${tableId} tbody`);
    if (!tbody) return;
    tbody.innerHTML = "";
    records.forEach(record => {
      let row = "<tr>";
      columns.forEach(col => row += `<td>${record[col] || ""}</td>`);
      row += "</tr>";
      tbody.innerHTML += row;
    });
  }

  // Patients
  populateTable("patientsTable", loadData("patients"),
    ["name", "gender", "diagnosis", "treatment", "discharge_details"]);

  // BFCI
  populateTable("bfciTable", loadData("bfci"),
    ["mother_name", "child_name", "dob", "age_months", "weight", "height", "immunization_status"]);

  // MCH
  populateTable("mchTable", loadData("mch"),
    ["mother_name", "visit_date", "gestational_age", "visit_reason", "child_name"]);

  // Surveillance
  populateTable("surveillanceTable", loadData("surveillance"),
    ["reporting_officer", "disease_suspected", "date_reported", "number_cases", "number_deaths", "location"]);

  // IDSR
  populateTable("idsrTable", loadData("idsr"),
    ["reporting_officer", "disease_name", "date_reported", "number_cases", "number_deaths", "district"]);

  // Immunization
  populateTable("immunizationTable", loadData("immunization"),
    ["child_name", "mother_name", "dob", "bcg", "opv0", "opv1", "measles"]);

  // Occupational Health
  populateTable("occupationalTable", loadData("occupational_health"),
    ["workplace_name", "area", "hazards_identified", "incidents_reported", "date_reported", "risk_level"]);

  // Contact
  populateTable("contactTable", loadData("contact"),
    ["name", "email", "message"]);
}

// === Home Info (unchanged) ===
function showHomeInfo(topic) {
  // ... keep your existing switch cases ...
}

// === Initialize ===
document.addEventListener('DOMContentLoaded', function () {
  showTab('home');
});










