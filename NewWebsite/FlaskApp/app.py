from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template("signup.html")

@app.route("/signup",methods=['POST'])
def signup():
    _name = request.form('name')
    _password = request.form('password')
    _email = request.form('email')
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
if __name__ == "__main":
    app.run()