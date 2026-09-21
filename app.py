from flask import flask
app = flask(__name__)

@app.route("/")
def home():
    return "My to-do website is working!"

if __name__ == "_main_":
    app.run(debug=True)
