from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to represent doctors and their schedules
doctors = [
  {
      "id": 1,
      "name": "Dr. Smith",
      "max_patients": 10,
      "days_available": ["Monday", "Wednesday", "Friday"],
  },
  {
      "id": 2,
      "name": "Dr. Johnson",
      "max_patients": 8,
      "days_available": ["Tuesday", "Thursday", "Saturday"],
  },
]

# Sample data to represent booked appointments
appointments = [
  {
    "patient_id": 101,
    "name": "Amita",
    "apt_timings": "18:00",
    "apt_date": "Wednesday",
  },
  {
    "patient_id": 102,
    "name": "Akshay",
    "apt_timings": "17:30",
    "apt_date": "Tuesday",
  },
]

# Doctor Listing Endpoint
@app.route("/doctors", methods=["GET"])
def get_doctors():
  return jsonify(doctors)

# Doctor Detail Endpoint
@app.route("/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):
  doctor = next((d for d in doctors if d["id"] == doctor_id), None)  ## checking if the doctor with "doctor_id" is available
  if doctor:
      return jsonify(doctor)
  else:
      return jsonify({"error": "Doctor not found"}), 404


# Appointment Booking Endpoint
@app.route("/appointments", methods=["POST"])
def book_appointment():
  data = request.json
  doctor_id = data.get("doctor_id")
  
  doctor = next((d for d in doctors if d["id"] == doctor_id), None)
  
  if not doctor:
      return jsonify({"error": "Doctor not found"}), 404

  if len(appointments) >= doctor["max_patients"]:
      return jsonify({"error": "Doctor is fully booked"}), 400

  appointments.append(data)
  return jsonify({"message": "Appointment booked successfully"})

if __name__ == "__main__":
  app.run(debug=True)
