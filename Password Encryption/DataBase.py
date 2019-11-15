import nacl.secret
import nacl.utils

#user_NonceKey = {}


def database_editor(user_nonce_key, account_n):
    """This uses the function used for editing the present user database.
    user_nonce_key is the present user database. It is a dictionary which stores the account name as the key and
    the value represents the (nonce, key) tuple. """
    if user_nonce_key.get(account_n, 0) != 0:
        print("An Account with the same name already exists in your profile do you want to overwrite it?")
        x = input("Yes or No ")
        if x == "Yes":
            nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
            key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
            user_nonce_key[account_n] = (nonce, key)
            return user_nonce_key
        elif x == "No":
            return user_nonce_key
        else:
            print("Enter a valid input")
            return user_nonce_key
    else:
        nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        user_nonce_key[account_n] = (nonce, key)
        return user_nonce_key


#user_NonceKey["MID"] = (0, 0)
#user_NonceKey = database_editor(user_NonceKey, "M.I.D")

#account_name = input("Enter Account name")
#passwordx = input("Enter the password")


def password_encryptor(user_nonce_key, account_n, password, length=16):
    """This function is used for password encryption. It first checks if the account exists in th use database.
    Then it uses the account name to excess the (nonce, key) and use it for the encryption
    and returns an encrypted password.
    """
    if user_nonce_key.get(account_n, 0) == 0:
        print("No account with the given name exists. Please recheck or create a new account encryption. ")
    else:
        length = int(length)
        password = bytes(password, 'utf-8')
        key = user_nonce_key[account_n][1]
        nonce = user_nonce_key[account_n][0]
        box = nacl.secret.SecretBox(key)
        encrypted = box.encrypt(password, nonce)
        encrypted = str(encrypted)
        encrypted = encrypted[10:length+10]
        return encrypted

#x = password_encryptor(user_NonceKey, account_name, passwordx)
#print(x)

