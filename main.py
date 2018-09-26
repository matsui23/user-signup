from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():

    return render_template('edit-html.html')
    

@app.route("/validate_info", methods = ['POST'])
def info_ctrl():
    user_name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    print(user_name)
    print(password)
    print(verify_password)
    print(email)
    return render_template('edit-html.html', username = user_name, password = password, 
    verify_password = verify_password, email = email)

app.run()