from flask import Flask, render_template, request, flash
import math

app = Flask(__name__)
app.secret_key = "Harsh_Secret_Key_HEHE"

def convert_to_metric(weight_lbs, height_inches):

    return weight_lbs * 0.453592, height_inches * 2.54

def calculate_bmi(weight_kg, height_cm):
    h = height_cm / 100
    if h <= 0:
        return None
    return weight_kg / (h * h)

def classify_bmi(bmi):
    if bmi < 18.5:
        return {
            "category": "Underweight",
            "range": "BMI < 18.5",
            "color": "text-blue-600",
            "bg": "bg-blue-50",
            "border": "border-blue-200"
        }
    elif bmi < 25:
        return {
            "category": "Normal weight",
            "range": "BMI 18.5 - 24.9",
            "color": "text-green-600",
            "bg": "bg-green-50",
            "border": "border-green-200"
        }
    elif bmi < 30:
        return {
            "category": "Overweight",
            "range": "BMI 25 - 29.9",
            "color": "text-yellow-600",
            "bg": "bg-yellow-50",
            "border": "border-yellow-200"
        }
    else:
        return {
            "category": "Obesity",
            "range": "BMI ≥ 30",
            "color": "text-red-600",
            "bg": "bg-red-50",
            "border": "border-red-200"
        }

def validate_input(weight, height, system):
   
    try:
        w = float(weight)
        h = float(height)
    except:
        return "Enter valid numbers."

    if w <= 0 or h <= 0:
        return "Height and weight must be positive."

    if system == "metric":
        if not (50 <= h <= 300):
            return "Height should be between 50–300 cm."
        if not (20 <= w <= 500):
            return "Weight should be between 20–500 kg."
    else:
        if not (20 <= h <= 120):
            return "Height should be between 20–120 inches."
        if not (40 <= w <= 1100):
            return "Weight should be between 40–1100 lbs."

    return None


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    unit_system = "metric"
    height = ""
    weight = ""

    if request.method == "POST":
        unit_system = request.form.get("unitSystem", "metric")
        height = request.form.get("height", "")
        weight = request.form.get("weight", "")

        err = validate_input(weight, height, unit_system)
        if err:
            flash(err, "danger")
            return render_template("index.html",
                                   unit_system=unit_system,
                                   height=height,
                                   weight=weight,
                                   result=None)

        if unit_system == "metric":
            w_kg = float(weight)
            h_cm = float(height)
        else:
            w_kg, h_cm = convert_to_metric(float(weight), float(height))

        bmi = calculate_bmi(w_kg, h_cm)
        if bmi is None or not math.isfinite(bmi):
            flash("Something went wrong with the calculation.", "danger")
            return render_template("index.html",
                                   unit_system=unit_system,
                                   height=height,
                                   weight=weight,
                                   result=None)

        info = classify_bmi(bmi)
        result = {"bmi": f"{bmi:.1f}", **info}

    return render_template("index.html",
                           unit_system=unit_system,
                           height=height,
                           weight=weight,
                           result=result)


if __name__ == "__main__":
    app.run(debug=True)
