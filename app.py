from flask import Flask, request, Response

app = Flask(__name__)

# Dane logowania
USERNAME = 'admin'
PASSWORD = 'pass'


# Funkcja uwierzytelniająca
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD


# Funkcja błędu uwierzytelnienia
def authentication_failed():
    return Response('Nieprawidłowe dane logowania', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


# Funkcja chroniona uwierzytelnianiem
@app.route('/')
def index():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authentication_failed()
    return '<h1>Zalogowano pomyślnie!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
