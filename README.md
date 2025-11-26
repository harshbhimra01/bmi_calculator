
# BMI Calculator (Flask)

A simple web app that lets you calculate your Body Mass Index (BMI).
Supports both **metric** (kg/cm) and **imperial** (lbs/in) units.

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/74038190/240825379-0db32290-c193-4b32-95dc-413ce9e446a5.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxODkzNjUsIm5iZiI6MTc2NDE4OTA2NSwicGF0aCI6Ii83NDAzODE5MC8yNDA4MjUzNzktMGRiMzIyOTAtYzE5My00YjMyLTk1ZGMtNDEzY2U5ZTQ0NmE1LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTExMjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMTI2VDIwMzEwNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZiMTBmNDYyYzMwYzExYTlkNjYyYzc1NGY5NWJjMjZhNWM1YWIyMzAyZmM0YzA3MThhZDlkNWQxOTIxMTNmMDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.upLzyEOoytRVB73M4ofRgSz0D8ECiuQfqjv-P89mSmQ" width="650">
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

