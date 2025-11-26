
# BMI Calculator (Flask)

A simple web app that lets you calculate your Body Mass Index (BMI).
Supports both **metric** (kg/cm) and **imperial** (lbs/in) units.

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/74038190/240885602-330af13b-6435-4505-8a02-1869b677f9eb.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxODkzNjUsIm5iZiI6MTc2NDE4OTA2NSwicGF0aCI6Ii83NDAzODE5MC8yNDA4ODU2MDItMzMwYWYxM2ItNjQzNS00NTA1LThhMDItMTg2OWI2NzdmOWViLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTExMjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMTI2VDIwMzEwNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZiMTQwZjEzZjdiODQxMTQyYjdjNjQ2NjFjN2Y4NDBlOGRkYTIxZTRlMTlmNTVmZWU1ZTNlNGNjMzdmNjkwMmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.S6PoT-MYGy-iTfdIsYbbAO6l2avn1TeR7rMPn74aX0U" width="650">
</p>

---

## What this app does

* Lets you switch between metric and imperial units
* Calculates BMI and shows the category (underweight, normal, etc.)
* Has a clean, minimal UI
* Basic validation + error messages
* Runs on Flask (Python)

Nothing fancy — just a straightforward BMI calculator that works.

---

## BMI Categories (Quick Reference)

| Category      | BMI Value      |
| ------------- | -------------- |
| Underweight   | Less than 18.5 |
| Normal Weight | 18.5–24.9      |
| Overweight    | 25–29.9        |
| Obesity       | 30 or above    |

---

## How to run it

Make sure you’re using **Python 3**.

Clone the repo and install the dependencies:

```bash
git clone <your-repo-url>
cd bmi-calculator
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## Setting up the secret key

In `app.py`, add:

```python
import secrets
app.secret_key = secrets.token_hex(16)
```

This is just for session messages; don’t worry too much about it for local development.

---

## Folder structure

```
bmi-calculator/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## How BMI is calculated

**Metric:**

```
BMI = weight_kg / (height_m)^2
```

**Imperial:**

```
BMI = (weight_lbs / (height_in)^2) * 703
```

---

## Possible future additions

* Dark mode
* BMI tracking/history
* Minor UI improvements
* Better validation

---

## Want to contribute?

Feel free to open an issue or send a PR.

---

