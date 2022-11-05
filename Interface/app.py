from flask import  Flask, render_template, redirect, url_for

app = Flask(__name__)

# @app.route('/home')
# def home():
#     return render_template('index.html')


@app.route('/')
def signup():
    return render_template('login/signup.html')

@app.route('/login/')
def login():
    return render_template('login/login.html')

if __name__ == '__main__':
    app.run(debug = True)