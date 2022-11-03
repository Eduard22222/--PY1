import string
from random import sample


def get_random_password(count_sym=8) -> str:
    password_list = []
    password = []
    while len(password_list) < count_sym:
        password_list.append(sample(string.digits, 1))
        password_list.append(sample(string.ascii_lowercase, 1))
        password_list.append(sample(string.ascii_uppercase, 1))
    password_list = sample(password_list, count_sym)
    for i in password_list:
        for n in i:
            password.append(n)
    password = ''.join(password)
    return password


print(get_random_password())
