
from flask import Flask, request, Response
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "")

    # VULNERABILIDAD INTENCIONAL: el parámetro se inserta
    # directamente en HTML sin escapar.
    return Response(
        f"<html><body><h1>Hello, {name}!</h1></body></html>",
        mimetype="text/html"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
