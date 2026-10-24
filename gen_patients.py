#!/usr/bin/env python3
"""Generate 10 fake patients for the LinkRTC web demo.

Output matches the mobile app's profile shape exactly:
  conditions[], medications[], allergies[], medical_history, biomarkers,
  smoking_status (never|former|current),
  alcohol_use (none|occasional|moderate|heavy),
  pregnancy_status (not_pregnant|pregnant|unsure|not_applicable),
  travel_radius_miles

All data is INVENTED. No real people.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "patients")
os.makedirs(OUT, exist_ok=True)

PATIENTS = [
    {
        "id": 1, "name": "Ava Thompson", "age": 34, "sex": "female",
        "conditions": ["Breast Cancer", "Hypertension"],
        "medications": ["Tamoxifen", "Lisinopril"],
        "allergies": ["Penicillin"],
        "medical_history": "Lumpectomy 2023. Family history of breast cancer.",
        "biomarkers": "ER+/PR+, HER2-",
        "smoking_status": "never",
        "alcohol_use": "occasional",
        "pregnancy_status": "not_pregnant",
        "travel_radius_miles": 50,
    },
    {
        "id": 2, "name": "Marcus Reed", "age": 58, "sex": "male",
        "conditions": ["Type 2 Diabetes", "Coronary Artery Disease"],
        "medications": ["Metformin", "Atorvastatin", "Aspirin"],
        "allergies": ["Sulfa drugs"],
        "medical_history": "Stent placement 2021. Hospitalized for chest pain 2020.",
        "biomarkers": "A1C 7.8, LDL 95",
        "smoking_status": "former",
        "alcohol_use": "moderate",
        "pregnancy_status": "not_applicable",
        "travel_radius_miles": 25,
    },
    {
        "id": 3, "name": "Sofia Alvarez", "age": 29, "sex": "female",
        "conditions": ["Rheumatoid Arthritis"],
        "medications": ["Methotrexate", "Folic Acid"],
        "allergies": ["Latex", "Ibuprofen"],
        "medical_history": "Diagnosed 2022. No surgeries.",
        "biomarkers": "RF positive, anti-CCP high",
        "smoking_status": "never",
        "alcohol_use": "none",
        "pregnancy_status": "pregnant",
        "travel_radius_miles": 10,
    },
    {
        "id": 4, "name": "James Okafor", "age": 47, "sex": "male",
        "conditions": ["Chronic Kidney Disease", "Hypertension"],
        "medications": ["Losartan", "Furosemide"],
        "allergies": [],
        "medical_history": "CKD stage 3. On low-sodium diet.",
        "biomarkers": "eGFR 42, Creatinine 1.9",
        "smoking_status": "never",
        "alcohol_use": "none",
        "pregnancy_status": "not_applicable",
        "travel_radius_miles": 100,
    },
    {
        "id": 5, "name": "Emily Chen", "age": 41, "sex": "female",
        "conditions": ["Multiple Sclerosis"],
        "medications": ["Ocrelizumab", "Vitamin D"],
        "allergies": ["Codeine"],
        "medical_history": "Relapsing-remitting MS since 2019.",
        "biomarkers": "MRI: 4 lesions",
        "smoking_status": "former",
        "alcohol_use": "occasional",
        "pregnancy_status": "not_pregnant",
        "travel_radius_miles": 50,
    },
    {
        "id": 6, "name": "David Nguyen", "age": 63, "sex": "male",
        "conditions": ["Parkinson's Disease"],
        "medications": ["Levodopa", "Carbidopa"],
        "allergies": ["Shellfish"],
        "medical_history": "Diagnosed 2020. Mild tremor, right hand.",
        "biomarkers": "",
        "smoking_status": "never",
        "alcohol_use": "none",
        "pregnancy_status": "not_applicable",
        "travel_radius_miles": 25,
    },
    {
        "id": 7, "name": "Olivia Martins", "age": 26, "sex": "female",
        "conditions": ["Asthma", "Eczema"],
        "medications": ["Albuterol", "Fluticasone"],
        "allergies": ["Peanuts", "Dust mites"],
        "medical_history": "Childhood asthma. ER visit 2019.",
        "biomarkers": "IgE elevated",
        "smoking_status": "never",
        "alcohol_use": "occasional",
        "pregnancy_status": "unsure",
        "travel_radius_miles": 10,
    },
    {
        "id": 8, "name": "Robert Hayes", "age": 71, "sex": "male",
        "conditions": ["Prostate Cancer", "Type 2 Diabetes"],
        "medications": ["Leuprolide", "Metformin"],
        "allergies": ["Iodine contrast"],
        "medical_history": "Prostatectomy 2022. Diabetes 15 years.",
        "biomarkers": "PSA 0.4, A1C 8.1",
        "smoking_status": "former",
        "alcohol_use": "moderate",
        "pregnancy_status": "not_applicable",
        "travel_radius_miles": 50,
    },
    {
        "id": 9, "name": "Grace Kim", "age": 38, "sex": "female",
        "conditions": ["Crohn's Disease"],
        "medications": ["Adalimumab", "Azathioprine"],
        "allergies": [],
        "medical_history": "Bowel resection 2021. Flare 2023.",
        "biomarkers": "CRP 12, Calprotectin high",
        "smoking_status": "current",
        "alcohol_use": "none",
        "pregnancy_status": "not_pregnant",
        "travel_radius_miles": 100,
    },
    {
        "id": 10, "name": "Daniel Foster", "age": 52, "sex": "male",
        "conditions": ["Melanoma", "Hypertension"],
        "medications": ["Pembrolizumab", "Amlodipine"],
        "allergies": ["Aspirin"],
        "medical_history": "Stage II melanoma excised 2024.",
        "biomarkers": "BRAF V600E positive",
        "smoking_status": "former",
        "alcohol_use": "heavy",
        "pregnancy_status": "not_applicable",
        "travel_radius_miles": 25,
    },
]

PROFILE_FIELDS = [
    "conditions", "medications", "allergies", "medical_history",
    "biomarkers", "smoking_status", "alcohol_use", "pregnancy_status",
    "travel_radius_miles",
]

index = []
for p in PATIENTS:
    # Per-patient file: app-shaped profile + a little display metadata.
    profile = {k: p[k] for k in PROFILE_FIELDS}
    out = {
        "id": p["id"],
        "name": p["name"],
        "age": p["age"],
        "sex": p["sex"],
        "profile": profile,
    }
    path = os.path.join(OUT, f"patient-{p['id']}.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    # Index entry: enough to render the list, not the full record.
    index.append({
        "id": p["id"],
        "name": p["name"],
        "age": p["age"],
        "sex": p["sex"],
        "summary": ", ".join(p["conditions"]),
        "file": f"patients/patient-{p['id']}.json",
    })

with open(os.path.join(HERE, "patients.json"), "w") as f:
    json.dump({"patients": index}, f, indent=2)

print(f"Wrote {len(PATIENTS)} patient files + patients.json")
