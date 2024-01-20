from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "zzharrybin219"
app.config['MYSQL_DB'] = "demo"
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signup():
    if request.method == "POST":
        _name = request.form('name')
        _password = request.form('password')
        _email = request.form('email')

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO customer (user_name,user_username,user_password) VALUES (%s,%s,%s)",(_name,_password,_email))
        mysql.connection.commit()
        cursor.close()

        return "Bạn đã đăng ký thành công"
    return json.dumps({'html':'<span>All fields good !!</span>'})
if __name__ == "__main":
    app.run()