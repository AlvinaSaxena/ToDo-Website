from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{os.path.join(basedir, "todo.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
     sno=db.Column(db.Integer, primary_key=True)
     title=db.Column(db.String(200), nullable=False)
     desc=db.Column(db.String(500), nullable=False)
     date_created=db.Column(db.DateTime, default=datetime.utcnow)

     def __repr__(self) -> str:
          return f"{self.sno} - {self.title}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin/', methods=['GET','POST'])
def signin():
    return render_template('signin.html')

@app.route('/TodoApp/', methods=['GET','POST'])
def adding_todos():
        if request.method=='POST':
            return render_template('main.html')
        
@app.route('/show/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    return render_template('main.html', allTodo=allTodo)


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/feedback/')
def feedback():
    return render_template('feedback.html')


@app.route('/delete/<int:sno>')
def delete(sno):
    todo= Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/show/')

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/show/')
    todo= Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
