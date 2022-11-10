from flask import  Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'jkuatjuja239836'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=300)

db = SQLAlchemy(app)


class users(db.Model):
    


@app.route('/', methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('user', usr = username))
    else:
        return render_template('login/signup.html')
        

@app.route('/login/', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session.permanent = True
        session['user'] = username
        flash('Login Successfull')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Already logged in')
            return redirect(url_for('user'))
        return render_template('login/login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('landing/landing.html', usr = user)
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    # if 'user' in session:
    #     user = session['user']
    flash('You have been logged out','info')
    session.pop('user', None)
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug = True)