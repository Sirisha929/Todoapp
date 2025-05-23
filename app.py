from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, due_date TEXT, priority TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY due_date")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    due_date = request.form['due_date']
    priority = request.form['priority']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, due_date, priority) VALUES (?, ?, ?)",
              (title, due_date, priority))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        c.execute("UPDATE tasks SET title=?, due_date=?, priority=? WHERE id=?",
                  (title, due_date, priority, id))
        conn.commit()
        return redirect(url_for('index'))
    c.execute("SELECT * FROM tasks WHERE id=?", (id,))
    task = c.fetchone()
    conn.close()
    return render_template('edit.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
 
