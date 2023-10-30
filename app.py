from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

# database models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    
@app.route('/')
def index():
    books = Book.query.all()  
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    new_book = Book(title=title)
    db.session.add(new_book)
    db.session.commit()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)