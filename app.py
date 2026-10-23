from flask import Flask,redirect,render_template,request,url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html",tasks = tasks)

@app.route("/add", methods = ["POST"])
def add_task():
    task = request.form.get("task","").strip()

    if task:
        tasks.append({"text": task, "done": False})
    return redirect(url_for("home"))

@app.route("/toggle/<int:task_index>", methods = ["POST"])
def toggle_task(task_index):
    if 0<= task_index < len(tasks):
        tasks[task_index]["done"]= not tasks[task_index]["done"]
    return redirect(url_for("home"))

@app.route("/delete/<int:task_index>",methods = ["POST"])
def delete_task(task_index):
    if 0<= task_index<len(tasks):
        tasks.pop(task_index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
