import time

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
    if bcrypt.checkpw(encode_password(user_input_pwd), hashed_pwd):
        print("Passwords match")
    else:
        print("Passwords don't match")


def hash_user_pwd():
    byte_pwd = encode_password(ask_password())
    salt = generate_salt(16)
    return hash_pwd(byte_pwd, salt)


def calculate_time_cost():
    user_pwd = ask_password()
    for i in range(4, 24):
        ts_salt_start = time.time()
        salt = generate_salt(i)
        ts_salt_end_hash_start = time.time()
        hash_pwd(encode_password(user_pwd), salt)
        ts_hash_end = time.time()
        salt_cost = ts_salt_end_hash_start - ts_salt_start
        hash_cost = ts_hash_end - ts_salt_end_hash_start
        print(salt_cost)
        print(hash_cost)


if __name__ == '__main__':
    # hashed_pwd = hash_user_pwd()
    # check_pwd(hashed_pwd)
    calculate_time_cost()
