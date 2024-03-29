from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/first')
def first_endpoint():
    response = jsonify({"message": "First endpoint reached"})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'
    return response

@app.route('/second')
def second_endpoint():
    response = jsonify({"param1": "value1", "param2": "value2"})
    response.status_code = 400
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'
    return response

if __name__ == '__main__':
    app.run(debug=True)
