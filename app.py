import sqlite3

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

DATABASE = "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        """)


create_database()


@app.route("/")
def home():
    with get_connection() as connection:
        tasks = connection.execute(
            "SELECT id, text, done FROM tasks ORDER BY id DESC"
        ).fetchall()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task", "").strip()

    if task:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO tasks (text, done) VALUES (?, ?)",
                (task, 0)
            )

    return redirect(url_for("home"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    with get_connection() as connection:
        connection.execute(
            "UPDATE tasks SET done = NOT done WHERE id = ?",
            (task_id,)
        )

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_connection() as connection:
        connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

    return redirect(url_for("home"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    with get_connection() as connection:
        task = connection.execute(
            "SELECT id, text, done FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        if task is None:
            abort(404)

        if request.method == "POST":
            updated_text = request.form.get("text", "").strip()

            if updated_text:
                connection.execute(
                    "UPDATE tasks SET text = ? WHERE id = ?",
                    (updated_text, task_id)
                )

            return redirect(url_for("home"))

    return render_template("edit.html", task=task)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)