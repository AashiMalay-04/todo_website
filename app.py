from flask import Flask,redirect,render_template,request,url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html",tasks = tasks)

@app.post("/add")
def add_task():
    task = request.form.get("task","").strip()

    if task:
        tasks.append(task)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
