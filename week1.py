# CareFlow - Patient Event Log Generator

from datetime import datetime, timedelta

start_time = datetime.strptime("10:00", "%H:%M")

print(start_time)

new_time = start_time + timedelta(minutes=10)

print(new_time)

patient_001 = {
    "patient_id": "P001",

    "activities": [
        "Registration",
        "Vitals",
        "Triage",
        "Doctor",
        "Billing Counter",
        "Pathology",
        "X-Ray",
        "X-Ray report",
        "Doctor",
        "Pathology report",
        "Doctor",
        "Pharmacy",
        "Discharge"
    ],

    "timestamps": [
        "10:00",
        "10:10",
        "10:15",
        "10:25",
        "10:35",
        "10:50",
        "11:20",
        "11:55",
        "12:20",
        "14:00",
        "14:30",
        "14:40",
        "14:45"
    ]
}
patient_002 = {
    "patient_id": "P002",

    "activities": [
        "Registration",
        "Vitals",
        "Triage",
        "Doctor",
        "Billing Counter",
        "X-Ray",
        "Pathology",
        "X-Ray report",
        "Pathology report",
        "Triage",
        "Doctor",
        "Pharmacy",
        "Discharge"
    ],

    "timestamps": [
        "09:00",
        "09:15",
        "09:20",
        "09:30",
        "09:55",
        "10:40",
        "11:00",
        "11:10",
        "14:20",
        "14:30",
        "15:00",
        "15:50",
        "16:00"
    ]
}
patient_003 = {
    "patient_id": "P003",

    "activities": [
        "Registration",
        "Vitals",
        "Triage",
        "Doctor",
        "Pathology",
        "Pathology report",
        "Doctor",
        "Pharmacy",
        "Discharge"
    ],

    "timestamps": [
        "10:00",
        "10:15",
        "10:30",
        "12:55",
        "13:30",
        "15:55",
        "16:25",
        "16:50",
        "17:30"
    ]
}


def print_patient(patient):

    print("Case_ID", "Activity_Name", "Timestamp")

    for i in range(len(patient["activities"])):
        print(
            patient["patient_id"],
            patient["activities"][i],
            patient["timestamps"][i]
        )



patients = [
    patient_001,
    patient_002,
    patient_003
]

for patient in patients:
    print_patient(patient)