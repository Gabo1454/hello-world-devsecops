from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)