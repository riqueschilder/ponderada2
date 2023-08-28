from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Leopoldo2019!@database/mydb'
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    todo = db.Column(db.String(200), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

def create_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            token = create_token(username)
            session['token'] = token
            return redirect(url_for('todolist'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/todolist', methods=['GET', 'POST'])
def todolist():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['username']
        if request.method == 'POST':
            new_todo = request.form['todo']
            todo_item = TodoItem(username=username, todo=new_todo)
            db.session.add(todo_item)
            db.session.commit()
        
        todos = TodoItem.query.filter_by(username=username).all()
        return render_template('todolist.html', username=username, todos=todos)
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
