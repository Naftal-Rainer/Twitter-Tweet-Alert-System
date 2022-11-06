from flask import  Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'jkuatjuja239836'
app.permanent_session_lifetime = timedelta(minutes=300)

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

if __name__ == '__main__':
    app.run(debug = True)