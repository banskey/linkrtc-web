# LinkRTC — Patient Sender (Web Demo)

A static website (GitHub Pages) that holds 10 **made-up** patients and lets you
pick one to send to the LinkRTC phone app. All data is fictional.

## How it works

- `index.html` — the page. Shows the 10 patients, lets you pick one.
- `patients.json` — the list the page reads.
- `patients/patient-N.json` — one file per patient, in the phone app's exact
  profile shape (`conditions`, `medications`, `allergies`, `smoking_status`,
  `alcohol_use`, `pregnancy_status`, etc).

When you pick a patient, the page shows a link like:

```
https://<you>.github.io/linkrtc-web/patients/patient-5.json
```

The phone app asks for that link and gets **only that one patient**.

> **Note:** GitHub Pages serves any file to anyone who knows its name. This is a
> hackathon demo with fake data, so that is fine. Do not put real patient data here.

## Run it locally

```
cd linkrtc-web
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000

## Regenerate the patients

```
python3 gen_patients.py
```

## Patient JSON shape

```json
{
  "id": 5,
  "name": "Emily Chen",
  "age": 41,
  "sex": "female",
  "profile": {
    "conditions": ["Multiple Sclerosis"],
    "medications": ["Ocrelizumab", "Vitamin D"],
    "allergies": ["Codeine"],
    "medical_history": "Relapsing-remitting MS since 2019.",
    "biomarkers": "MRI: 4 lesions",
    "smoking_status": "former",
    "alcohol_use": "occasional",
    "pregnancy_status": "not_pregnant",
    "travel_radius_miles": 50
  }
}
```
