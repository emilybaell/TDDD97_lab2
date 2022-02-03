from flask import Flask
app = Flask(__name__)

#app.debug = True


@app.route("/")
def home():
    return "Hello, Flask!"

def Function_name():
    return "jajamän"

def sign_in():
    return "fett signat asså"

def sign_up():
    return "tjusigt värre"

def sign_out():
    return "kunde inte bli bättre"

def Change_password():
    return "oj va bytt"

def get_user_data_by_token():
    return "tjusigt värre"

def get_user_data_by_email():
    return "ooj"

def Get_user_messages_by_token():
    return "tok-igt"

def get_user_messages_by_email():
    return "mailmail"

def post_message():
    return "värsta meddelandet"




if __name__=="__main__":
    app.run(debug=True)