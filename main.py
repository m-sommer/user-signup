from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup_form.html')

@app.route('/welcome')
def welcome():
    username = request.args.get("username")
    return render_template('welcome_greeting.html', username=username)

@app.route('/', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a valid username"
        username = ''
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "That's not a valid password"
        password = ''

    if verify_password == '' or verify_password != password:
        verify_password_error = "Passwords don't match"
        verify_password = ''
    
    """
    def multiple_at_signs():
        count = 0
        for char in email:
            if char == '@':
                count = count + 1
            if count > 1:
                return True
    """
    
    at_count = 0
    for char in email:
        if char == '@':
            at_count += 1
    
    period_count = 0
    for char in email:
        if char == '.':
            period_count += 1

    if email != "":   
        if len(email) < 3 or len(email) > 20 or ' ' in email or '@' not in email or '.' not in email or at_count > 1 or period_count > 1:
            email_error = "That's not a valid email"
            email = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect("/welcome?username=" + username)
    else:
        return render_template('signup_form.html',
            username=username,
            email=email,
            username_error=username_error, 
            password_error=password_error, 
            verify_password_error=verify_password_error,
            email_error=email_error)

app.run()