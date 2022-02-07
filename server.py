import email
from flask import Flask, jsonify
from itsdangerous import json
app = Flask(__name__)
import database_helper

app.debug = True


# @app.route("/")
# def home(): 
#     sign_in()
#     return "Hello, Flask!"

@app.route("/sign_in")
def sign_in(email, password):
    return jsonify(email="b@gmail.com")

@app.route("/sign_up")
def sign_up(email, password, firstname, familyname, gender, city, country):
    return "tjusigt värre"

@app.route("/sign_out")
def sign_out(token):
    return "kunde inte bli bättre"

@app.route("/Change_password")
def Change_password(token, oldPassword, newPassword):
    return "oj va bytt"

@app.route("/get_user_data_by_token")
def get_user_data_by_token(token):
    return "tjusigt värre"

@app.route("/get_user_data_by_email")
def get_user_data_by_email(token,email):
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)
 
@app.route("/Get_user_messages_by_token")
def Get_user_messages_by_token(token):
    return "tok-igt"

@app.route("/get_user_messages_by_email")
def get_user_messages_by_email(token, email):
    return "mailmail"

@app.route("/post_message")
def post_message(token, message, email):
    return "värsta meddelandet"




if __name__=="__main__":
    app.run()