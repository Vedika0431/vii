from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operator = data['operator']

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero!"
        else:
            result = "Invalid operation!"
    except ValueError:
        result = "Error: Enter valid numbers!"

    return jsonify({'result': result})

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
    

    #ipconfig /flushdns