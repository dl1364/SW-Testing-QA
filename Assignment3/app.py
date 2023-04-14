from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])

def template():
    if request.method == 'POST':
        weight = request.form.get('weight')
        feet = request.form.get('feet')
        inches = request.form.get('inches')
        bmi = calculate_bmi(feet, inches, weight)
        category = calculate_category(bmi)
        return render_template("template.html", feet=feet, inches=inches, weight=weight, bmi=bmi, category=category)
    else:
        return render_template("template.html")

def calculate_bmi(feet, inches, weight):
    float(inches)
    weight = float(weight) * .45
 
    addInches = float(feet) * 12
    newInches = float(inches) + addInches
    newHeight = float(newInches) * .025
    squareHeight = float(newHeight) * newHeight
    bmi = weight / squareHeight
    return round(bmi, 1)

def calculate_category(bmi):
    if bmi > 0 and bmi < 18.5:
        return "Underweight"
    elif bmi > 18.5 and bmi < 24.9 or bmi == 18.5 or bmi == 24.9:
        return "Normal Weight"
    elif bmi > 25 and bmi < 29.9 or bmi == 25 or bmi == 29.9:
        return "Overweight"
    elif bmi > 30 or bmi == 30:
        return "Obese"
    else:
        return "Error"


if __name__ == "__main__":
    app.run()