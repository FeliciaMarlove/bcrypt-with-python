import time

import bcrypt

import csv


def ask_password():
    return input('Please enter your password ')


def encode_password(pwd):
    return pwd.encode('utf-8')


def hash_pwd(pwd, salt):
    return bcrypt.hashpw(pwd, salt)


def generate_salt(rounds):
    return bcrypt.gensalt(rounds)


def check_pwd(hashed_pwd):
    user_input_pwd = input('Please enter your password again ')
    if bcrypt.checkpw(encode_password(user_input_pwd), hashed_pwd):
        print("Passwords match")
    else:
        print("Passwords don't match")


def get_user_pwd_hash():
    byte_pwd = encode_password(ask_password())
    salt = generate_salt(16)
    return hash_pwd(byte_pwd, salt)


def get_time_cost(lower_bound, upper_bound):
    user_pwd = ask_password()
    results = []
    for i in range(lower_bound, upper_bound + 1):
        ts_salt_start = time.time()
        salt = generate_salt(i)
        ts_salt_end_hash_start = time.time()
        hash_pwd(encode_password(user_pwd), salt)
        ts_hash_end = time.time()
        salt_cost = ts_salt_end_hash_start - ts_salt_start
        hash_cost = ts_hash_end - ts_salt_end_hash_start
        results.append([i, salt_cost, hash_cost])
    return results


def write_results_in_csv_file(results):
    csv_file = open('cost_results.csv', 'w')
    writer = csv.writer(csv_file)
    header = []
    data = []
    for result in results:
        header.append(result[0])
        data.append(result[2])
    writer.writerow(header)
    writer.writerow(data)


if __name__ == '__main__':
    # hashed_pwd = get_user_pwd_hash()
    # check_pwd(hashed_pwd)
    results_matrix = get_time_cost(4, 23)
    write_results_in_csv_file(results_matrix)
