import bcrypt


def ask_password():
    return input('Please enter your password')


def encode_password(pwd):
    return pwd.encode('utf-8')


def hash_pwd(pwd, salt):
    return bcrypt.hashpw(pwd, salt)


def generate_salt(rounds):
    return bcrypt.gensalt(rounds)


def check_pwd(hashed_pwd):
    user_input_pwd = input('Please enter your password again')
    return bcrypt.checkpw(user_input_pwd.encode('utf-8'), hashed_pwd)


if __name__ == '__main__':
    byte_pwd = encode_password(ask_password())
    salt = generate_salt(16)
    hashed_pwd = hash_pwd(byte_pwd, salt)
    if check_pwd(hashed_pwd):
        print("Passwords match")
    else:
        print("Passwords don't match")