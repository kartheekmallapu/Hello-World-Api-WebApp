from flask import Flask, jsonify, request
import os

app = Flask(__name__)
apimessage = [
  { 'message': 'Hello-World' }
]

@app.route('/apimessage')
def hello():
    return jsonify(apimessage)
@app.route('/index')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Web App Home Page</title>
</head>
<body>
    <h2>
        Hello World!
    </h2>
</body>
</html>'''
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
