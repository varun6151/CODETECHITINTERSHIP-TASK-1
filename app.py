from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi_route():
    data = request.get_json()
    weight = data['weight']
    height = data['height']
    
    if weight <= 0 or height <= 0:
        return jsonify({"error": "Weight and height must be positive values."}), 400
    
    bmi = calculate_bmi(weight, height)
    if bmi < 18.5:
        classification = "You are underweight."
    elif 18.5 <= bmi < 24.9:
        classification = "You have a normal weight."
    elif 25 <= bmi < 29.9:
        classification = "You are overweight."
    else:
        classification = "You are obese."
    
    return jsonify({"bmi": bmi, "classification": classification})

if __name__ == '__main__':
    app.run(debug=True)
