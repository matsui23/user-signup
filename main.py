from flask import Flask, request, redirect, render_template, url_for
import cgi
import validate_username
import validate_password
import validate_email

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
##Error Handlers    
    error_username = validate_username.validate(user_name)
    error_password = validate_password.validate_pass(password, verify_password)
    error_email = validate_email.validate_email(email)
##Testprints
    print(user_name)
    print(password)
    print(verify_password)
    print(email)

    if not error_username and not error_password and not error_email:
        return redirect(url_for('welcome_page',user_name=request.form.get("username")),code=307)

    return render_template('edit-html.html', username = user_name, password = password, 
    verify_password = verify_password, email = email, error_username = error_username
    , error_password = error_password, error_email = error_email)

@app.route("/welcome_page", methods=['POST', 'GET'])
def welcome_page():
    user_name = request.form.get('username')
    return render_template('welcome.html', username = user_name)


app.run()