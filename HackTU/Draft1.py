from flask import Flask, redirect, url_for, request
from cryptography.fernet import Fernet


#key = Fernet.generate_key()
key = b'03NwpyBGWTq9-B9M0-qk80uGLjm33yiK3nHLsjI0XTI='


def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    result = ""
    s = 26 - s
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def encryptor(p, u, key=b'03NwpyBGWTq9-B9M0-qk80uGLjm33yiK3nHLsjI0XTI='):
    p = str(p)
    u = len(u)
    p = encrypt(p, u)
    f = Fernet(key)
    p = bytes(p, 'utf-8')
    encrypt_value = f.encrypt(p)
    encrypt_value_str = str(encrypt_value, 'utf-8')
    print(encrypt_value_str[16:32])
    return encrypt_value_str[16:32]


app = Flask(__name__)

@app.route('/success/<password>')
def success(password):
   return 'Your encrypted password is %s' % password

@app.route('/login',methods = ['POST', 'GET'])

def login():
    if request.method == 'POST':
        username = request.form['nn']
        password = request.form['nm']
        password = encryptor(password, username)
        return redirect(url_for('success', password=password))


if __name__ == '__main__':
   app.run(debug = True)

