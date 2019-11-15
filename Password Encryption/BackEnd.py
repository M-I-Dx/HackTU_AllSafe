from DataBase import password_encryptor
from flask import Flask, redirect, url_for, request

# This is just an example of a potential database
user_database = {'Gmail': (b'\xe5\xc6{l\xd2\x06.\x91\x15w<9-\xed\xf69\x8dw\xc3H\x15\xb7\x00\xb1',
                           b'\xa4\xa5\xbfS\x11\xd2\xc31s{$\x01\x0fN\xc7\x132\x9e^\xe9Z\xa4/r\xe3\xc4g\xa7\xc9\xd3\xd8\xc9')}

app = Flask(__name__)


@app.route('/success/<password>')
def success(password):
    return 'Your encrypted password is %s' % password


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['nn']
        password = request.form['nm']
        password = password_encryptor(user_database, username, password)
        return redirect(url_for('success', password=password))


if __name__ == '__main__':
    app.run(debug=True)
