import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/hello', methods=['GET']) 
def helloworld():
    data = {"data": "Helloo World"}
    return jsonify(data)

@app.route('/operation', methods=["POST"])
def calculate():
    # JSON veriyi al
    data = request.get_json()

    # Verileri kontrol et
    if not data or 'number1' not in data or 'operator' not in data or 'number2' not in data:
        return jsonify(error="Eksik veya hatalı veri"), 400

    # Değişkenleri ata
    num1 = int(data['number1'])
    op = data['operator']
    num2 = int(data['number2'])

    # Hesaplama
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return jsonify(error="Sıfıra bölme hatası"), 400
        result = num1 / num2
    else:
        return jsonify(error="Geçersiz operatör"), 400

    # JSON yanıtını oluştur
    response = {"result": result}

    # Yanıtı geri gönder
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
