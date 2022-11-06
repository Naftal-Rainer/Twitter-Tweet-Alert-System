from flask import  Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

app.secret_key = 'jkuatjuja239836'

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
        session['user'] = username
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login/login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('landing/landing.html', usr = user)
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug = True)