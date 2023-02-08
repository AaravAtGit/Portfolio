from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.app_context().push()
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/')
def todo_list():
    todos = Todo.query.all()
    # print(todos[0])
    return render_template('todo_list.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = Todo(content=request.form['todo'])
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
