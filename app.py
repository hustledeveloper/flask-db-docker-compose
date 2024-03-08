import re
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/hello', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        data = {"data": "Hello World"} 
        return jsonify(data)
    
@app.route('/operation', methods=["POST"])
def calculate():
    num1 = request.form['number1']
    op = request.form['operator']
    num2 = request.form['number2']
    
    result = 1
    if op == '+':
          result = int(num1) + int(num2);
   
    if op == '-':
          result = int(num1) - int(num2);

    if op == '*':
          result = int(num1) * int(num2);

    if op == '/':
          result = int(num1) / int(num2);

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
