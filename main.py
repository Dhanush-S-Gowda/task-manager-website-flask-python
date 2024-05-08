from flask import Flask, render_template, request, redirect, url_for
from database import DataBase

app = Flask(__name__)

@app.template_filter('enumerate')
def jinja2_enumerate(iterable, start=0):
    return zip(range(start, len(iterable) + start), iterable)

def get_db():
    db = DataBase()
    return db

@app.route('/')
def index():
    db = get_db()
    tasks = db.return_data()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['newtask']
    db = get_db()
    db.add_data(task_name)
    return redirect(url_for('index'))

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete_task(name):
    if request.method == 'POST':
        db = get_db()
        result = db.delete_data(name)
        return redirect(url_for('index'))


@app.route('/update/<old_name>', methods=['POST'])
def update_task(old_name):
    if request.method == 'POST':
        new_name = request.json.get('newName')  
        status = request.json.get('status') 
        db = get_db()
        result = db.update_data(old_name, new_name, status)
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
